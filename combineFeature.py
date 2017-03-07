import numpy as np
import myLoadData

class combineFeature:
    featureNum = 0
    combineNum = 0
    featureCombineMap = []
    def __init__(self, featureNum, combineNum):
        self.featureNum = featureNum
        self.combineNum = combineNum
        self.__combineFun(0, 0, )

    def __combineFun(self, considerFeatureNo, alreadyCombine, *combine):
        # print(*combine)
        if alreadyCombine == self.combineNum:
            # print(combine)
            self.featureCombineMap.append(combine)
            return
        elif considerFeatureNo>=self.featureNum:
            return

        self.__combineFun(considerFeatureNo+1, alreadyCombine, *combine)

        self.__combineFun(considerFeatureNo + 1, alreadyCombine + 1, *combine, considerFeatureNo)
        # self.__combineFun(considerFeatureNo + 1, alreadyCombine + 1, *combine + (considerFeatureNo,))

    def outputCombineMap(self):
        # self.__combineFun(0,0,)
        print(self.featureCombineMap)

    def makeCombineData(self, dataX):
        print(dataX)
        print(dataX.shape[0])

        combineData = [] ##所有样本的所有组合
        for sample in dataX:
            combineSample = [] ##一个样本的所有组合
            print(sample)
            for combine in self.featureCombineMap:
                # print(combine)
                combineTemp = [] ###一个组合
                for column in combine:
                    # print(column)
                    combineTemp.append(sample[column])

                combineSample.append(combineTemp)

            # print(np.array(combineSample))
            # break;
            combineData.append(combineSample)
            # break;
        # print(combineData)

        return np.array(combineData)

a = combineFeature(4,2)
a.outputCombineMap()
irisData = myLoadData.loadIris()
b = a.makeCombineData(irisData.IrisDataTrainX)
# print(b)
# print(b.shape)




