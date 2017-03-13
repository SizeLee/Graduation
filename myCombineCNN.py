import numpy as np
import copy
import convLayer
import maxPoolingLayer
import fullConnect
import combineFeature
import combineNumCalculate

#for test
import myLoadData
import dataLossSimulator


class myCombineCNN:
    def __init__(self, data, combineNumConv1, convCoreNum1, combineNumPooling1):
        self.data = data
        self.combineNumConv1 = combineNumConv1
        self.combConvLayer1 = None
        self.convCoreNum1 = convCoreNum1
        self.convCoreList1 = list()
        self.convCoreOut1 = list()
        self.poolingCoreList1 = list()
        self.poolingCoreOut1 = list()

        self.combineNumPooling1 = combineNumPooling1
        self.combPoolingLayer1 = None

        self.allConnectData = None
        self.fullInputLayer = None

        self.midACData = None
        self.fullMidLayer = None

        self.predictResult = None

        self.poolingSFlist = None
        self.convSFlist = None


    def trainCNN(self, trainRound, trainRate):

        self.combConvLayer1 = combineFeature.combineFeature(self.data.DataX.shape[1], self.combineNumConv1)
        combKindNumConv1 = combineNumCalculate.combineNumCal(self.data.DataX.shape[1], self.combineNumConv1)
        inputDataX = self.combConvLayer1.makeCombineData(self.data.DataTrainX)

        for i in range(self.convCoreNum1):

            convCoreTemp = convLayer.convLayerCore(inputDataX, inputDataX.shape[2], trainRate)
            self.convCoreList1.append(convCoreTemp)
            self.convCoreOut1.append(convCoreTemp.calculate())

        self.combPoolingLayer1 = combineFeature.combineFeature(combKindNumConv1, self.combineNumPooling1)
        combKindNumPooling1 = combineNumCalculate.combineNumCal(combKindNumConv1, self.combineNumPooling1)

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



    #todo def runCNN(self):






irisDATA = myLoadData.loadIris()
mcnn = myCombineCNN(irisDATA, 2, 5, 4)
mcnn.trainCNN(1000,0.1)






# self.data = None
# if dataName == 'Iris':
#     self.data = myLoadData.loadIris()
# else:
#     print('No such data file, Waiting for new data set\n')
#     exit(1) # todo throw error or set new data






