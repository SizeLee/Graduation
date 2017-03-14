import numpy as np
import copy
import convLayer
import maxPoolingLayer
import fullConnect
import combineFeature
import combineNumCalculate
import costFunc

#for test
import myLoadData
import dataLossSimulator
import accuracyEvaluate


class myCombineCNN:
    def __init__(self, data, combineNumConv1, convCoreNum1, combineNumPooling1):
        self.data = data
        self.combineNumConv1 = combineNumConv1
        self.combConvLayer1 = None
        self.convCoreNum1 = convCoreNum1
        self.convCoreList1 = list()
        self.convCoreOut1 = None
        self.poolingCoreList1 = list()
        self.poolingCoreOut1 = None

        self.combineNumPooling1 = combineNumPooling1
        self.combPoolingLayer1 = None

        self.allConnectData = None
        self.fullInputLayer = None

        self.midACData = None
        self.fullMidLayer = None

        self.predictResult = None

        self.poolingSFlist = None
        self.convSFlist = None

        self.trainInitializeFlag = False


    def trainCNN(self, trainRound, trainRate):

        self.combConvLayer1 = combineFeature.combineFeature(self.data.DataX.shape[1], self.combineNumConv1)
        combKindNumConv1 = combineNumCalculate.combineNumCal(self.data.DataX.shape[1], self.combineNumConv1)
        inputDataX = self.combConvLayer1.makeCombineData(self.data.DataTrainX)

        self.convCoreOut1 = list()
        for i in range(self.convCoreNum1):

            convCoreTemp = convLayer.convLayerCore(inputDataX, inputDataX.shape[2], trainRate)
            self.convCoreList1.append(convCoreTemp)
            self.convCoreOut1.append(convCoreTemp.calculate())

        self.combPoolingLayer1 = combineFeature.combineFeature(combKindNumConv1, self.combineNumPooling1)
        combKindNumPooling1 = combineNumCalculate.combineNumCal(combKindNumConv1, self.combineNumPooling1)

        self.poolingCoreOut1 = list()
        for i in range(self.convCoreNum1):

            inputPoolingData = self.combPoolingLayer1.makeCombineData(self.convCoreOut1[i])
            poolingCoreTemp = maxPoolingLayer.maxPoolingLayerCore(inputPoolingData)
            self.poolingCoreList1.append(poolingCoreTemp)
            self.poolingCoreOut1.append(poolingCoreTemp.calculate())

        for i in range(self.convCoreNum1):

            if self.allConnectData is None:
                self.allConnectData = self.poolingCoreOut1[i]
            else:
                self.allConnectData = np.hstack((self.allConnectData, self.poolingCoreOut1[i]))

        # print(self.allConnectData)
        # print(self.allConnectData.shape)

        self.fullInputLayer = fullConnect.fullConnectInputLayer(self.allConnectData, trainRate)
        self.midACData = self.fullInputLayer.calculate()
        self.fullMidLayer = fullConnect.fullConnectMidLayer(self.midACData,self.data.DataTrainY,trainRate)
        self.predictResult = self.fullMidLayer.calculate()

        # print(self.predictResult)
        # print(self.data.DataTrainY)
        # print(self.predictResult.shape)
        # print(self.data.DataTrainY.shape)

        # todo BP process
        ####### full connect BP
        formerLayerSF = self.fullMidLayer.BP()
        # print(formerLayerSF)
        # print(formerLayerSF.shape)
        formerLayerSF = self.fullInputLayer.BP(formerLayerSF)
        # print(formerLayerSF)

        ####### max pooling layer BP
        splitStep = int(formerLayerSF.shape[1] / self.convCoreNum1)

        self.poolingSFlist = list()
        for i in range(self.convCoreNum1):
            SFtemp = formerLayerSF[:, i * splitStep : (i + 1) * splitStep].copy()
            # print(SFtemp.shape)
            self.poolingSFlist.append(SFtemp)

        formerLayerSF = list()
        for i in range(self.convCoreNum1):
            formerLayerSF.append(self.poolingCoreList1[i].BP(self.poolingSFlist[i]))

        # print(formerLayerSF[0])

        ######################    combine feature BP

        self.convSFlist = list()
        for i in range(self.convCoreNum1):
            self.convSFlist.append(self.combPoolingLayer1.BP(formerLayerSF[i]))

        # print(formerLayerSF)
        # print(formerLayerSF[0].shape)
        # print(len(formerLayerSF))

        #####################   conv layer BP
        for i in range(self.convCoreNum1):
            self.convCoreList1[i].BP(self.convSFlist[i])

        self.trainInitializeFlag = True

        ###################### start train in round
        for trainTime in range(trainRound-1):
            self.forwardPropagation()
            self.backPropagation()
            trainCost = costFunc.costCal(self.predictResult, self.data.DataTrainY)
            # self.forwardPropagation(self.combConvLayer1.makeCombineData(self.data.DataValX))
            # valCost = costFunc.costCal(self.predictResult, self.data.DataValY)
            # print(trainCost, valCost)
            print(trainCost)

        print(accuracyEvaluate.classifyAccuracyRate(self.predictResult, self.data.DataTrainY))

        self.forwardPropagation(self.combConvLayer1.makeCombineData(self.data.DataTestX))
        print(self.predictResult)
        print(costFunc.costCal(self.predictResult, self.data.DataTestY))
        print(self.data.DataTestY)
        print(accuracyEvaluate.classifyAccuracyRate(self.predictResult, self.data.DataTestY))


    def forwardPropagation(self, inputDataX = None):

        if self.trainInitializeFlag == False:
            print("Can\'t forwardPropagation CNN before train initialize\n")
            exit(1)#todo throw out error

        # self.combConvLayer1 = combineFeature.combineFeature(self.data.DataX.shape[1], self.combineNumConv1)
        # combKindNumConv1 = combineNumCalculate.combineNumCal(self.data.DataX.shape[1], self.combineNumConv1)
        # inputDataX = self.combConvLayer1.makeCombineData(self.data.DataTrainX)
        if inputDataX is None:
            inputDataX = self.combConvLayer1.makeCombineData(self.data.DataTrainX)

        self.convCoreOut1 = list()
        for i in range(self.convCoreNum1):

            self.convCoreOut1.append(self.convCoreList1[i].calculate(inputDataX))

        # self.combPoolingLayer1 = combineFeature.combineFeature(combKindNumConv1, self.combineNumPooling1)
        # combKindNumPooling1 = combineNumCalculate.combineNumCal(combKindNumConv1, self.combineNumPooling1)

        self.poolingCoreOut1 = list()
        for i in range(self.convCoreNum1):
            inputPoolingData = self.combPoolingLayer1.makeCombineData(self.convCoreOut1[i])
            self.poolingCoreOut1.append(self.poolingCoreList1[i].calculate(inputPoolingData))

        self.allConnectData = None
        for i in range(self.convCoreNum1):

            if self.allConnectData is None:
                self.allConnectData = self.poolingCoreOut1[i]
            else:
                self.allConnectData = np.hstack((self.allConnectData, self.poolingCoreOut1[i]))

        # print(self.allConnectData)
        # print(self.allConnectData.shape)

        # self.fullInputLayer = fullConnect.fullConnectInputLayer(self.allConnectData, trainRate)
        self.midACData = self.fullInputLayer.calculate(self.allConnectData)
        # self.fullMidLayer = fullConnect.fullConnectMidLayer(self.midACData, self.data.DataTrainY, trainRate)
        self.predictResult = self.fullMidLayer.calculate(self.midACData)

        # print(self.predictResult)

    def backPropagation(self):
        ####### full connect BP
        formerLayerSF = self.fullMidLayer.BP()
        # print(formerLayerSF)
        # print(formerLayerSF.shape)
        formerLayerSF = self.fullInputLayer.BP(formerLayerSF)
        # print(formerLayerSF)

        ####### max pooling layer BP
        splitStep = int(formerLayerSF.shape[1] / self.convCoreNum1)

        self.poolingSFlist = list()
        for i in range(self.convCoreNum1):
            SFtemp = formerLayerSF[:, i * splitStep: (i + 1) * splitStep].copy()
            # print(SFtemp.shape)
            self.poolingSFlist.append(SFtemp)

        formerLayerSF = list()
        for i in range(self.convCoreNum1):
            formerLayerSF.append(self.poolingCoreList1[i].BP(self.poolingSFlist[i]))

        # print(formerLayerSF[0])

        ######################    combine feature BP

        self.convSFlist = list()
        for i in range(self.convCoreNum1):
            self.convSFlist.append(self.combPoolingLayer1.BP(formerLayerSF[i]))

        # print(formerLayerSF)
        # print(formerLayerSF[0].shape)
        # print(len(formerLayerSF))

        #####################   conv layer BP
        for i in range(self.convCoreNum1):
            self.convCoreList1[i].BP(self.convSFlist[i])



    #todo def runCNN(self):


irisDATA = myLoadData.loadIris(0.3, -1)
mcnn = myCombineCNN(irisDATA, 2, 5, 4)
mcnn.trainCNN(2000,0.1)






# self.data = None
# if dataName == 'Iris':
#     self.data = myLoadData.loadIris()
# else:
#     print('No such data file, Waiting for new data set\n')
#     exit(1) # todo throw error or set new data






