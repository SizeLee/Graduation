import numpy as np
import myLoadData
import combineFeature
import convLayer

class maxPoolingLayerCore:

    def __init__(self, inputDataX):

        self.__inputDataX = inputDataX.copy()
        self.__poolingSize = inputDataX.shape[2]
        self.__poolingPosition = None
        self.__outputDataX = None

    def calculate(self):

        self.__outputDataX = np.max(self.__inputDataX, axis=2) ##obtain max of each row in each sample, it's max pooling
        self.__poolingPosition = np.argmax(self.__inputDataX, axis=2) ##obtain taking value's position, for latter BP process
        # print(self.__outputDataX)
        # print(self.__poolingPosition)

        return self.__outputDataX.copy()

    def outputCalculateResult(self):
        print(self.__outputDataX)


    #todo def BP function


# irisData = myLoadData.loadIris()
# comb = combineFeature.combineFeature(4,2)
# inputDataX = comb.makeCombineData(irisData.DataTestX)
# testConvCore = convLayer.convLayerCore(inputDataX, inputDataX.shape[2])
# convOut = testConvCore.calculate()
# # print(convOut)
# comb2 = combineFeature.combineFeature(6,4)
# # comb2.outputCombineMap()
# inputPoolingDataX = comb2.makeCombineData(convOut)
# # print(inputPoolingDataX)
# testPoolingCore = maxPoolingLayerCore(inputPoolingDataX)
# result = testPoolingCore.calculate()
# print(result)
# result[:,:]=1
# testPoolingCore.outputCalculateResult()

