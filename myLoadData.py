import numpy as np
import random
import dataLossSimulator
class loadIris:
    # DataX = None
    # DataTrainX = None
    # DataValX = None
    # DataTestX = None
    #
    # DataY = None
    # DataTrainY = None
    # DataTestY = None
    # DataValY = None
    #
    # sampleList = None
    # sampleX = None
    # sampleY = None

    dataName = 'Iris'

    def __init__(self, lossRate = 0, setlossValue = 0):
        fp = open('..\\iris.txt','r') #todo change the way open file

        self.DataX = None
        self.DataTrainX = None
        self.DataTrainXLoss = None
        self.DataValX = None
        self.DataValXLoss = None
        self.DataTestX = None
        self.DataTestXLoss = None

        self.DataY = None
        self.DataTrainY = None
        self.DataTestY = None
        self.DataValY = None

        self.sampleList = None
        self.sampleX = None
        self.sampleY = None

        self.lossRate = lossRate
        self.setLossValue = setlossValue

        sampleCount = 0
        self.sampleList = []
        for line in fp:
            sampleCount += 1
            line = line.rstrip('\n')
            dataStrList = line.split(',')
            linetemp = []
            for data in dataStrList:
                if data == 'Iris-setosa':
                    linetemp.append([1,0,0])
                elif data == 'Iris-versicolor':
                    linetemp.append([0,1,0])
                elif data == 'Iris-virginica':
                    linetemp.append([0,0,1])
                elif linetemp == []:
                    linetemp.append([float(data)])
                else:
                    linetemp[0].append(float(data))
            # print(linetemp)
            self.sampleList.append(linetemp)

        # print(self.sampleList)
        # print(sampleCount)
        ##load into memory
        orderList = range(sampleCount)
        randomChange = random.sample(orderList,sampleCount)
        # print(randomChange)
        # randomChange.sort()
        # print(randomChange)
        sampleTemp = self.sampleList.copy()
        for i in orderList:
            self.sampleList[i] = sampleTemp[randomChange[i]]

        # print(sampleList)

        self.sampleX = []
        self.sampleY = []

        for line in self.sampleList:
            self.sampleX.append(line[0])
            self.sampleY.append(line[1])

        self.DataX = np.array(self.sampleX)
        self.DataY = np.array(self.sampleY,dtype=float)

        # print(self.IrisDataX)
        # print(self.IrisDataY)

        self.DataTrainX = self.DataX[:int(0.6 * sampleCount), :]
        self.DataTrainY = self.DataY[:int(0.6 * sampleCount), :]

        self.DataValX = self.DataX[int(0.6 * sampleCount):int(0.8 * sampleCount), :]
        self.DataValY = self.DataY[int(0.6 * sampleCount):int(0.8 * sampleCount), :]

        self.DataTestX = self.DataX[int(0.8 * sampleCount):, :]
        self.DataTestY = self.DataY[int(0.8 * sampleCount):, :]

        fp.close()

        # print(self.DataTrainX.shape)
        # print(self.DataTrainY.shape)
        #
        # print(self.DataValX.shape)
        # print(self.DataValY.shape)
        #
        # print(self.DataTestX.shape)
        # print(self.DataTestY.shape)

        self.lossSimulator = dataLossSimulator.dataLossSimulator(self.DataX.shape[1], self.lossRate, self.setLossValue)

        self.DataTrainXLoss = self.lossSimulator.lossSimulate(self.DataTrainX)
        self.DataValXLoss = self.lossSimulator.lossSimulate(self.DataValX)
        self.DataTestXLoss = self.lossSimulator.lossSimulate(self.DataTestX)

        self.DataTrainX = self.DataTrainXLoss
        self.DataValX = self.DataValXLoss
        self.DataTestX = self.DataTestXLoss



# loadiris = loadIris()