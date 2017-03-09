import numpy as np
import myLoadData

class combineFeature:
    # __featureNum = 0
    # __combineNum = 0
    # __featureCombineMap = []

    def __init__(self, featureNum, combineNum):
        self.__featureNum = 0
        self.__combineNum = 0
        self.__featureCombineMap = []

        self.__featureNum = featureNum
        self.__combineNum = combineNum
        self.__combineFun(0, 0, )

    def __combineFun(self, considerFeatureNo, alreadyCombine, *combine):
        # print(*combine)
        if alreadyCombine == self.__combineNum:
            # print(combine)
            self.__featureCombineMap.append(combine)
            return
        elif considerFeatureNo >= self.__featureNum:
            return

        self.__combineFun(considerFeatureNo+1, alreadyCombine, *combine)

        self.__combineFun(considerFeatureNo + 1, alreadyCombine + 1, *combine, considerFeatureNo)
        # self.__combineFun(considerFeatureNo + 1, alreadyCombine + 1, *combine + (considerFeatureNo,))

    def outputCombineMap(self):
        # self.__combineFun(0,0,)
        print(self.__featureCombineMap)

    def makeCombineData(self, dataX):
        # print(dataX)
        # print(dataX.shape[0])

        combineData = [] ##所有样本的所有组合
        for sample in dataX:
            combineSample = [] ##一个样本的所有组合
            # print(sample)
            # print(len(sample.shape))
            if len(sample.shape) > 2:
                print('Error in combineFeature: Can\'t support combine Data dim large than 3')

            elif len(sample.shape) == 2:
                if sample.shape[0] > 1 and sample.shape[1] > 1:
                    print('Error in  combineFeature: Can\'t support combine Data Sample isn\'t line vector')

                elif sample.shape[0] > 1 and sample.shape[1] == 1:
                    sample = sample.transpose()[0]
                    # print(sample)


            for combine in self.__featureCombineMap:
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

    #todo def bp delt map generator



##########Test
# a = combineFeature(4,2)
# a.outputCombineMap()
# irisData = myLoadData.loadIris()
# b = a.makeCombineData(irisData.IrisDataTrainX)
# print(b)
# print(b.shape)
# a = combineFeature(6,4)
# a.outputCombineMap()




