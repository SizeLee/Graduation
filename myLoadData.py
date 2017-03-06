import numpy as np
import random
class loadIris:
    IrisDataX = None
    IrisDataTrainX = None
    IrisDataValX = None
    IrisDataTestX = None

    IrisDataY = None
    IrisDataTrainY = None
    IrisDataTestY = None
    IrisDataValY = None

    sampleList = None
    sampleX = None
    sampleY = None
    def __init__(self):
        fp = open('iris.txt')

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

        self.IrisDataX = np.array(self.sampleX)
        self.IrisDataY = np.array(self.sampleY,dtype=float)

        # print(self.IrisDataX)
        # print(self.IrisDataY)

        self.IrisDataTrainX = self.IrisDataX[:int(0.6 * sampleCount), :]
        self.IrisDataTrainY = self.IrisDataY[:int(0.6 * sampleCount), :]

        self.IrisDataValX = self.IrisDataX[int(0.6 * sampleCount):int(0.8 * sampleCount), :]
        self.IrisDataValY = self.IrisDataY[int(0.6 * sampleCount):int(0.8 * sampleCount), :]

        self.IrisDataTestX = self.IrisDataX[int(0.8 * sampleCount):, :]
        self.IrisDataTestY = self.IrisDataY[int(0.8 * sampleCount):, :]

        print(self.IrisDataTrainX.shape)
        print(self.IrisDataTrainY.shape)

        print(self.IrisDataValX.shape)
        print(self.IrisDataValY.shape)

        print(self.IrisDataTestX.shape)
        print(self.IrisDataTestY.shape)



loadiris = loadIris()