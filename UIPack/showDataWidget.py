from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QFont

class showDataItem(QWidget):
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



class ShowDataWidget(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()

        if self.parentW.dataFor[self.senderName] is None:
            labelbox = QHBoxLayout()
            labelbox.addStretch(1)
            label = QLabel('No Data For Show')
            label.setFont(QFont('微软雅黑', 28))
            labelbox.addWidget(label)
            labelbox.addStretch(1)
            layout.addLayout(labelbox)

        else:
            ####label for training data set##########
            layout.addStretch(1)
            label = QLabel('Trainning Data Set')
            label.setFont(QFont('微软雅黑', 12))
            layout.addWidget(label)

            ####list for training data set##############
            self.trainDataShowListWidget = QListWidget()
            # print(self.senderName)
            self.featureNum = self.parentW.dataFor[self.senderName].DataTrainX.shape[1]
            # print(self.featureNum)
            itemPattern = showDataItem(self.makeListFirstLine(self.featureNum))
            item = QListWidgetItem(self.trainDataShowListWidget)
            item.setSizeHint(itemPattern.sizeHint())
            self.trainDataShowListWidget.addItem(item)
            self.trainDataShowListWidget.setItemWidget(item, itemPattern)

            self.labelDic = {v:k for k,v in self.parentW.dataFor[self.senderName].yClassDic.items()}
            self.labelIndex = self.parentW.dataFor[self.senderName].DataTrainY.argmax(1)
            for i in range(self.parentW.dataFor[self.senderName].DataTrainX.shape[0]):
                content = []
                content.append('%5s' % str(i + 1))
                for j in range(self.featureNum):
                    content.append('%-8s' % str(self.parentW.dataFor[self.senderName].DataTrainX[i, j]))

                content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                content.append('%-15s' % str(self.parentW.dataFor[self.senderName].DataTrainY[i, :]))
                # print(content)
                itemPattern = showDataItem(content)
                item = QListWidgetItem(self.trainDataShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.trainDataShowListWidget.addItem(item)
                self.trainDataShowListWidget.setItemWidget(item, itemPattern)

            self.trainDataShowListWidget.resize(self.trainDataShowListWidget.sizeHint())
            layout.addWidget(self.trainDataShowListWidget)
            layout.addStretch(1)

            #########label for validation data set
            layout.addStretch(1)
            label = QLabel('Validation Data Set')
            label.setFont(QFont('微软雅黑', 12))
            layout.addWidget(label)

            #########list for validation data set
            self.valDataShowListWidget = QListWidget()
            # print(self.senderName)
            self.featureNum = self.parentW.dataFor[self.senderName].DataValX.shape[1]
            # print(self.featureNum)
            itemPattern = showDataItem(self.makeListFirstLine(self.featureNum))
            item = QListWidgetItem(self.valDataShowListWidget)
            item.setSizeHint(itemPattern.sizeHint())
            self.valDataShowListWidget.addItem(item)
            self.valDataShowListWidget.setItemWidget(item, itemPattern)

            self.labelDic = {v: k for k, v in self.parentW.dataFor[self.senderName].yClassDic.items()}
            self.labelIndex = self.parentW.dataFor[self.senderName].DataValY.argmax(1)
            for i in range(self.parentW.dataFor[self.senderName].DataValX.shape[0]):
                content = []
                content.append('%5s' % str(i + 1))
                for j in range(self.featureNum):
                    content.append('%-8s' % str(self.parentW.dataFor[self.senderName].DataValX[i, j]))

                content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                content.append('%-15s' % str(self.parentW.dataFor[self.senderName].DataValY[i, :]))
                # print(content)
                itemPattern = showDataItem(content)
                item = QListWidgetItem(self.valDataShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.valDataShowListWidget.addItem(item)
                self.valDataShowListWidget.setItemWidget(item, itemPattern)

            self.valDataShowListWidget.resize(self.valDataShowListWidget.sizeHint())
            layout.addWidget(self.valDataShowListWidget)
            layout.addStretch(1)

            ######label for test data set#####
            layout.addStretch(1)
            label = QLabel('Test Data Set')
            label.setFont(QFont('微软雅黑', 12))
            layout.addWidget(label)

            ######list for test data set###
            self.testDataShowListWidget = QListWidget()
            # print(self.senderName)
            self.featureNum = self.parentW.dataFor[self.senderName].DataTestX.shape[1]
            # print(self.featureNum)
            itemPattern = showDataItem(self.makeListFirstLine(self.featureNum))
            item = QListWidgetItem(self.testDataShowListWidget)
            item.setSizeHint(itemPattern.sizeHint())
            self.testDataShowListWidget.addItem(item)
            self.testDataShowListWidget.setItemWidget(item, itemPattern)

            self.labelDic = {v: k for k, v in self.parentW.dataFor[self.senderName].yClassDic.items()}
            self.labelIndex = self.parentW.dataFor[self.senderName].DataTestY.argmax(1)
            for i in range(self.parentW.dataFor[self.senderName].DataTestX.shape[0]):
                content = []
                content.append('%5s' % str(i + 1))
                for j in range(self.featureNum):
                    content.append('%-8s' % str(self.parentW.dataFor[self.senderName].DataTestX[i, j]))

                content.append('%-25s' % self.labelDic[self.labelIndex[i]])
                content.append('%-15s' % str(self.parentW.dataFor[self.senderName].DataTestY[i, :]))
                # print(content)
                itemPattern = showDataItem(content)
                item = QListWidgetItem(self.testDataShowListWidget)
                item.setSizeHint(itemPattern.sizeHint())
                self.testDataShowListWidget.addItem(item)
                self.testDataShowListWidget.setItemWidget(item, itemPattern)

            self.testDataShowListWidget.resize(self.testDataShowListWidget.sizeHint())
            layout.addWidget(self.testDataShowListWidget)
            layout.addStretch(1)




        self.setLayout(layout)
        self.setGeometry(400, 150, 1100, 800)
        self.setWindowTitle(self.Title)
        self.show()

    def makeListFirstLine(self, num):
        pattern = 'Feature'
        firstLine = list()
        firstLine.append('%-5s' % 'No.')
        for i in range(num):
            firstLine.append('%-8s' % (pattern + str(i+1)))
        firstLine.append('%-25s' % 'Label')
        firstLine.append('%-15s' % 'Label Vector')

        print(firstLine)
        return firstLine





