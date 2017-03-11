import numpy as np
import copy
import convLayer
import maxPoolingLayer
import fullConnect
import combineFeature

#for test
import myLoadData
import dataLossSimulator


class myCombineCNN:
    def __init__(self, dataName):
        self.data = None
        if dataName == 'Iris':
            self.data = myLoadData.loadIris()
        else:
            print('No such data file, Waiting for new data set\n')
            exit(1) # todo throw error or set new data




