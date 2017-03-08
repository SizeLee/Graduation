import numpy as np
import copy
import myLoadData
import combineFeature
import convLayer

class maxPoolingLayerCore:

    def __init__(self, inputDataX):

        self.__inputDataX = inputDataX
        self.__poolingSize = inputDataX.shape[2]
        self.__poolingPosition = np.zeros(inputDataX.shape)



irisData = myLoadData.loadIris()
comb = combineFeature.combineFeature(4,2)
inputDataX = comb.makeCombineData(irisData.IrisDataTestX)
testConvCore = convLayer.convLayerCore(inputDataX, inputDataX.shape[2])
convOut = testConvCore.calculator()
# print(convOut)
comb2 = combineFeature.combineFeature(6,4)
comb2.outputCombineMap()
inputPoolingDataX = comb2.makeCombineData(convOut)
print(inputPoolingDataX)
