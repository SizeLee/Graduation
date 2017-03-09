import numpy as np
import copy
import myLoadData
import combineFeature

class convLayerCore:
    def __init__(self, InputDataX, wLength ):
        self.__w = None
        self.__inputDataX = None
        self.__outputDataX = None
        sampleNum = InputDataX.shape[0]
        combineNum = InputDataX.shape[1]
        combineFeatureNum = InputDataX.shape[2]
        if wLength!=combineFeatureNum:
            print('Error in convlayer.Wrong conv core length')
            exit(1)#todo throw error

        self.__inputDataX = copy.deepcopy(InputDataX)

        self.__w = 0.24 * np.random.rand(wLength, 1) - 0.12
        # print(self.__w)


    def calculate(self):
        self.__outputDataX = np.dot(self.__inputDataX, self.__w)
        # print(np.dot(self.__inputDataX, self.__w).shape)
        for sample in self.__inputDataX:
            break;
            print(sample)
            outputSample = np.dot(sample, self.__w)
            print(self.__w)
            print(outputSample)

        return self.__outputDataX

    #todo def BP function


# irisData = myLoadData.loadIris()
# comb = combineFeature.combineFeature(4,2)
# inputDataX = comb.makeCombineData(irisData.IrisDataTestX)
# testConvCore = convLayerCore(inputDataX, inputDataX.shape[2])
# convOut = testConvCore.calculate()
# print(convOut)
# print(inputDataX)