import numpy as np
import activationFunction
import myLoadData


class fullConnectInputLayer:

    def __init__(self, inputDataX, trainRate, LoutinRate = 0.5):
        ''' inputDataX should be two dim, transpose 3dim data(sample, pooling data, core num)
                                     into two dim(sample, pooling data*core num) '''
        if len(inputDataX.shape) != 2:
            print("Error in fullConectLayer: inputDataX isn't 2 dim\n")
            exit(1) #todo throw error

        self.sampleNum = inputDataX.shape[0]
        self.__L_in = inputDataX.shape[1] + 1
        self.__LoutinRate = LoutinRate
        self.__L_out = int(np.floor(self.__LoutinRate * self.__L_in))
        self.epsilon = np.sqrt(6)/(np.sqrt(self.__L_in) + np.sqrt(self.__L_out))
        self.__w = np.random.rand(self.__L_in, self.__L_out) * 2 * self.epsilon - self.epsilon
        self.__inputDataX = np.hstack((np.ones((self.sampleNum, 1)), inputDataX))
        # print(self.__inputDataX)
        self.__outputDataX = None
        self.__outputDataAct = None
        self.__trainRate = trainRate


    def calculate(self, newInputDataX = None):

        if newInputDataX is not None:

            if self.__inputDataX[:, 1:].shape != newInputDataX.shape:
                print('Error in full connect input layer: new data is with wrong size\n')
                exit(1)  # todo throw out error
            else:
                self.__inputDataX = np.hstack((np.ones((self.sampleNum, 1)), newInputDataX))    ##########iterate new data into mid layer

        self.__outputDataX = np.dot(self.__inputDataX, self.__w)
        self.__outputDataAct = activationFunction.sigmoid(self.__outputDataX)

        return self.__outputDataAct.copy()

    #todo def BP function

    def BP(self, sensitivityFactor):
        delt = sensitivityFactor * activationFunction.sigmoidGradient(self.__outputDataX)
        wGradient = 1/self.sampleNum * np.dot(self.__inputDataX.T, delt)

        sensitivityFactorFormerLayer = np.dot(delt, self.__w[1:, :].T)
        self.__w = self.__w - self.__trainRate * wGradient

        return sensitivityFactorFormerLayer




class fullConnectMidLayer:

    def __init__(self, midInputDataX, y, trainRate):
        '''midInputDataX is sample * midfeature, y is sample * yLabel'''

        if len(midInputDataX.shape) != 2:
            print("Error in fullConectLayer: inputDataX isn't 2 dim")
            exit(1) #todo throw error

        self.sampleNum = midInputDataX.shape[0]
        self.__L_in = midInputDataX.shape[1] + 1
        self.__L_out = y.shape[1]
        self.epsilon = np.sqrt(6) / (np.sqrt(self.__L_in) + np.sqrt(self.__L_out))
        self.__w = np.random.rand(self.__L_in, self.__L_out) * 2 * self.epsilon - self.epsilon
        self.__midInputDataX = np.hstack((np.ones((self.sampleNum, 1)), midInputDataX))
        # print(self.__midInputDataX)
        self.__outputY = None
        self.__outputYAct = None
        self.__yLabel = y.copy()
        self.__trainRate = trainRate

    def calculate(self, newInputDataX = None):

        if newInputDataX is not None:

            if self.__midInputDataX[:, 1:].shape != newInputDataX.shape:
                print('Error in full connect mid layer: new data is with wrong size\n')
                exit(1)  # todo throw out error
            else:
                self.__midInputDataX = np.hstack((np.ones((self.sampleNum, 1)), newInputDataX))    ##########iterate new data into mid layer

        self.__outputY = np.dot(self.__midInputDataX, self.__w)
        self.__outputYAct = activationFunction.sigmoid(self.__outputY)

        return self.__outputYAct.copy()

    #todo def BP function
    def BP(self):
        delt = (self.__outputYAct - self.__yLabel) * activationFunction.sigmoidGradient(self.__outputY)
        wGradient = 1/self.sampleNum * np.dot(self.__midInputDataX.T, delt)
        sensitivityFactorFormerLayer = np.dot(delt, self.__w[1:,:].T)

        self.__w = self.__w - self.__trainRate * wGradient

        return sensitivityFactorFormerLayer



