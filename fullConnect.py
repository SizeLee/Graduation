import numpy as np
import activationFunction
import myLoadData


class fullConnectInputLayer:

    def __init__(self, inputDataX, LoutinRate = 0.5):
        ''' inputDataX should be two dim, transpose 3dim data(sample, pooling data, core num)
                                     into two dim(sample, pooling data*core num) '''
        if len(inputDataX.shape) != 2:
            print("Error in fullConectLayer: inputDataX isn't 2 dim\n")
            exit(1) #todo throw error

        self.__L_in = inputDataX.shape[1]
        self.__LoutinRate = LoutinRate
        self.__L_out = int(np.floor(self.__LoutinRate * self.__L_in))
        self.epsilon = np.sqrt(6)/(np.sqrt(self.__L_in) + np.sqrt(self.__L_out))
        self.__w = np.random.rand(self.__L_in, self.__L_out) * 2 * self.epsilon - self.epsilon
        self.__inputDataX = inputDataX.copy()
        self.__outputDataX = None
        self.__outputDataAct = None


    def calculate(self):

        self.__outputDataX = np.dot(self.__inputDataX, self.__w)
        self.__outputDataAct = activationFunction.sigmoid(self.__outputDataX)

        return self.__outputDataAct.copy()

    #todo def BP function



class fullConnectMidLayer:

    def __init__(self, midInputDataX, y):
        '''midInputDataX is sample * midfeature, y is sample * yLabel'''

        if len(midInputDataX.shape) != 2:
            print("Error in fullConectLayer: inputDataX isn't 2 dim")
            exit(1) #todo throw error

        self.__L_in = midInputDataX.shape[1]
        self.__L_out = y.shape[1]
        self.epsilon = np.sqrt(6) / (np.sqrt(self.__L_in) + np.sqrt(self.__L_out))
        self.__w = np.random.rand(self.__L_in, self.__L_out) * 2 * self.epsilon - self.epsilon
        self.__midInputDataX = midInputDataX.copy()
        self.__outputY = None
        self.__outputYAct = None

    def calculate(self):
        self.__outputY = np.dot(self.__midInputDataX, self.__w)
        self.__outputYAct = activationFunction.sigmoid(self.__outputY)

        return self.__outputYAct.copy()

    #todo def BP function










