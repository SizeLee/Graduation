from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QFont
from MyCombCNNPack import myException
import numpy as np

class showResultItem(QWidget):
    def __init__(self, contentList):
        super().__init__()
        self.contentList = contentList
        self.length = len(contentList)
        self.initUI()

    def initUI(self):
        self.labelList = list()
        layout = QHBoxLayout()
        for i in range(self.length):
            label = QLabel(self.contentList[i])
            label.setFont(QFont('微软雅黑', 12))
            self.labelList.append(label)
            layout.addWidget(label)
            layout.addStretch(1)

        self.setLayout(layout)
        self.resize(self.sizeHint())



class ShowResultWidget(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        if self.senderName == 'New':
            if self.parentW.mcbcnn is None:
                labelbox = QHBoxLayout()
                labelbox.addStretch(1)
                label = QLabel('No Existed Model For Show')
                label.setFont(QFont('微软雅黑', 28))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

            else:
######################train set result######
                try:
                    self.parentW.mcbcnn.runCNN(setChoose= 'Train', data = self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return


                ####label for training data set result##########
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Trainning Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                ####list for training data set result##############
                self.trainResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.mcbcnn.data.DataTrainY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.trainResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.trainResultShowListWidget.addItem(item)
                self.trainResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                self.labelIndex = self.parentW.mcbcnn.data.DataTrainY.argmax(1)
                self.prelabelIndex = self.parentW.mcbcnn.getPredictResult().argmax(1)

                for i in range(self.parentW.mcbcnn.data.DataTrainX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.mcbcnn.data.DataTrainY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.mcbcnn.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.trainResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.trainResultShowListWidget.addItem(item)
                    self.trainResultShowListWidget.setItemWidget(item, itemPattern)

                self.trainResultShowListWidget.resize(self.trainResultShowListWidget.sizeHint())
                layout.addWidget(self.trainResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of training data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)


###################validation set result #######
                try:
                    self.parentW.mcbcnn.runCNN(setChoose= 'Validation', data = self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return


                #########label for validation data set
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Validation Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                #########list for validation data set

                self.valResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.mcbcnn.data.DataValY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.valResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.valResultShowListWidget.addItem(item)
                self.valResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                self.labelIndex = self.parentW.mcbcnn.data.DataValY.argmax(1)
                self.prelabelIndex = self.parentW.mcbcnn.getPredictResult().argmax(1)

                for i in range(self.parentW.mcbcnn.data.DataValX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.mcbcnn.data.DataValY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.mcbcnn.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.valResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.valResultShowListWidget.addItem(item)
                    self.valResultShowListWidget.setItemWidget(item, itemPattern)

                self.valResultShowListWidget.resize(self.valResultShowListWidget.sizeHint())
                layout.addWidget(self.valResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of validation data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)


##########################test set result #######
                try:
                    self.parentW.mcbcnn.runCNN(setChoose='Test', data=self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                ######label for test data set#####
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Test Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                ######list for test data set###
                self.testResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.mcbcnn.data.DataTestY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.testResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.testResultShowListWidget.addItem(item)
                self.testResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                self.labelIndex = self.parentW.mcbcnn.data.DataTestY.argmax(1)
                self.prelabelIndex = self.parentW.mcbcnn.getPredictResult().argmax(1)

                for i in range(self.parentW.mcbcnn.data.DataTestX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.mcbcnn.data.DataTestY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.mcbcnn.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.testResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.testResultShowListWidget.addItem(item)
                    self.testResultShowListWidget.setItemWidget(item, itemPattern)

                self.testResultShowListWidget.resize(self.testResultShowListWidget.sizeHint())
                layout.addWidget(self.testResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of test data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)


            self.setLayout(layout)
            self.setGeometry(400, 150, 1100, 800)
            self.setWindowTitle(self.Title)
            self.show()


        elif self.senderName == 'Tra':
            if self.parentW.trann is None:
                labelbox = QHBoxLayout()
                labelbox.addStretch(1)
                label = QLabel('No Existed Model For Show')
                label.setFont(QFont('微软雅黑', 28))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

            else:
    ######################train set result######
                try:
                    self.parentW.trann.runCNN(setChoose='Train', data=self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                ####label for training data set result##########
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Trainning Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                ####list for training data set result##############
                self.trainResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.trann.data.DataTrainY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.trainResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.trainResultShowListWidget.addItem(item)
                self.trainResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                self.labelIndex = self.parentW.trann.data.DataTrainY.argmax(1)
                self.prelabelIndex = self.parentW.trann.getPredictResult().argmax(1)

                for i in range(self.parentW.trann.data.DataTrainX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.trann.data.DataTrainY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.trann.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.trainResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.trainResultShowListWidget.addItem(item)
                    self.trainResultShowListWidget.setItemWidget(item, itemPattern)

                self.trainResultShowListWidget.resize(self.trainResultShowListWidget.sizeHint())
                layout.addWidget(self.trainResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of training data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)

                ###################validation set result #######
                try:
                    self.parentW.trann.runCNN(setChoose='Validation', data=self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                #########label for validation data set
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Validation Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                #########list for validation data set

                self.valResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.trann.data.DataValY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.valResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.valResultShowListWidget.addItem(item)
                self.valResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                self.labelIndex = self.parentW.trann.data.DataValY.argmax(1)
                self.prelabelIndex = self.parentW.trann.getPredictResult().argmax(1)

                for i in range(self.parentW.trann.data.DataValX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.trann.data.DataValY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.trann.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.valResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.valResultShowListWidget.addItem(item)
                    self.valResultShowListWidget.setItemWidget(item, itemPattern)

                self.valResultShowListWidget.resize(self.valResultShowListWidget.sizeHint())
                layout.addWidget(self.valResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of validation data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)

                ##########################test set result #######
                try:
                    self.parentW.trann.runCNN(setChoose='Test', data=self.parentW.dataFor[self.senderName])

                except myException.DataExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed or Valid Data For Model Running')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.ModelExistException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('No Existed Model For Show')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataModelMatchException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Present Model Doesn\'t Match Present Data')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                except myException.DataValidFormatException:
                    labelbox = QHBoxLayout()
                    labelbox.addStretch(1)
                    label = QLabel('Data Format Error')
                    label.setFont(QFont('微软雅黑', 28))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)
                    layout.addLayout(labelbox)

                    self.setLayout(layout)
                    self.setGeometry(400, 150, 1100, 800)
                    self.setWindowTitle(self.Title)
                    self.show()

                    return

                ######label for test data set#####
                layout.addStretch(1)
                labelbox = QHBoxLayout()
                label = QLabel('Result on Test Data Set')
                label.setFont(QFont('微软雅黑', 12))
                labelbox.addWidget(label)
                labelbox.addStretch(1)
                layout.addLayout(labelbox)

                ######list for test data set###
                self.testResultShowListWidget = QListWidget()
                # print(self.senderName)
                self.labelVecLength = len(str(self.parentW.trann.data.DataTestY[0, :]))
                # print(self.featureNum)
                itemPattern = showResultItem(self.makeListFirstLine(self.labelVecLength))
                item = QListWidgetItem(self.testResultShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.testResultShowListWidget.addItem(item)
                self.testResultShowListWidget.setItemWidget(item, itemPattern)

                self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                self.labelIndex = self.parentW.trann.data.DataTestY.argmax(1)
                self.prelabelIndex = self.parentW.trann.getPredictResult().argmax(1)

                for i in range(self.parentW.trann.data.DataTestX.shape[0]):
                    content = []
                    content.append('%5s' % str(i + 1))
                    content.append('%-15s' % str(self.parentW.trann.data.DataTestY[i, :]))
                    content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                    content.append('%-25s' % self.labelDic[self.prelabelIndex[i]])
                    content.append('%-25s' % str(self.parentW.trann.getPredictResult()[i, :]))
                    # print(content)

                    itemPattern = showResultItem(content)
                    item = QListWidgetItem(self.testResultShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.testResultShowListWidget.addItem(item)
                    self.testResultShowListWidget.setItemWidget(item, itemPattern)

                self.testResultShowListWidget.resize(self.testResultShowListWidget.sizeHint())
                layout.addWidget(self.testResultShowListWidget)
                layout.addStretch(1)

                #######set percentage label of test data in label box
                classPercentageDic = self.calPercentage(self.labelDic, self.labelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (classPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    labelbox.addWidget(label)
                    labelbox.addStretch(1)

                prelabelBox = QHBoxLayout()
                label = QLabel('Prediction: ')
                label.setFont(QFont('微软雅黑', 12))
                prelabelBox.addWidget(label)
                prelabelBox.addStretch(1)
                preclassPercentageDic = self.calPercentage(self.labelDic, self.prelabelIndex)
                for eachKey in classPercentageDic:
                    label = QLabel('%s: %.2f%%' % (eachKey, (preclassPercentageDic[eachKey] * 100)))
                    label.setFont(QFont('微软雅黑', 12))
                    prelabelBox.addWidget(label)
                    prelabelBox.addStretch(1)
                layout.addLayout(prelabelBox)

            self.setLayout(layout)
            self.setGeometry(400, 150, 1100, 800)
            self.setWindowTitle(self.Title)
            self.show()


    def makeListFirstLine(self, labelVecLength):
        firstLine = list()
        firstLine.append('%-5s' % 'No.')
        labelVector = 'Label Vector'
        if labelVecLength > len(labelVector):
            addLength = labelVecLength - len(labelVector)
            for i in range(addLength):
                labelVector = labelVector + ' '

        firstLine.append(labelVector)

        pattern = 'Label'

        firstLine.append('%-25s' % pattern)
        firstLine.append('%-25s' % ('Predict ' + pattern))

        firstLine.append('%-15s' % 'Predict Label Vector')

        # print(firstLine)
        return firstLine

    def calPercentage(self, labelDic, labelIndex):
        classPercentageDic = {k: v for v, k in labelDic.items()}
        for eachKey in classPercentageDic:
            classPercentageDic[eachKey] = 0
        # print(classPercentageDic)

        sumSample = 0
        for each in labelIndex:
            classPercentageDic[labelDic[each]] += 1
            sumSample += 1
        # print(classPercentageDic)

        for eachKey in classPercentageDic:
            classPercentageDic[eachKey] /= float(sumSample)
        # print(classPercentageDic)

        return classPercentageDic

