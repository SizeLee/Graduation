from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QProgressBar, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import pyqtSignal
from MyCombCNNPack import myCombineCNN, traditionalNN, myException, Judgement
import re, threading, time


class showJudgeFactorItem(QWidget):
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
            label.setFont(QFont('Consolas', 12))
            self.labelList.append(label)
            layout.addWidget(label)
            layout.addStretch(1)

        self.setLayout(layout)
        self.resize(self.sizeHint())


class judgeWidget(QWidget):
    def __init__(self, Title, parentW, senderName, dataSetName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.dataSetName = dataSetName
        self.wlength = 900
        self.whigh = 900

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
                if self.dataSetName == 'Train':
                    try:
                        self.parentW.mcbcnn.runCNN(setChoose='Train', data=self.parentW.dataFor[self.senderName])

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

                    self.mj = Judgement.myJudge(self.parentW.mcbcnn.data.yClassDic,
                                                self.parentW.mcbcnn.getAccuratePredictResult().argmax(1),
                                                self.parentW.mcbcnn.data.DataTrainY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100, ))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)


########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.mcbcnn.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)


                elif self.dataSetName == 'Validation':
                    try:
                        self.parentW.mcbcnn.runCNN(setChoose='Validation', data=self.parentW.dataFor[self.senderName])

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

                    self.mj = Judgement.myJudge(self.parentW.mcbcnn.data.yClassDic,
                                                self.parentW.mcbcnn.getAccuratePredictResult().argmax(1),
                                                self.parentW.mcbcnn.data.DataValY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100,))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)

                    ########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.mcbcnn.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)



                elif self.dataSetName == 'Test':
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


                    self.mj = Judgement.myJudge(self.parentW.mcbcnn.data.yClassDic,
                                                self.parentW.mcbcnn.getAccuratePredictResult().argmax(1),
                                                self.parentW.mcbcnn.data.DataTestY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100,))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)

                    ########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.mcbcnn.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.mcbcnn.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)

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
                if self.dataSetName == 'Train':
                    try:
                        self.parentW.trann.runTraNN(setChoose='Train', data=self.parentW.dataFor[self.senderName])

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

                    self.mj = Judgement.myJudge(self.parentW.trann.data.yClassDic,
                                                self.parentW.trann.getAccuratePredictResult().argmax(1),
                                                self.parentW.trann.data.DataTrainY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100,))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)

                    ########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.trann.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)


                elif self.dataSetName == 'Validation':
                    try:
                        self.parentW.trann.runTraNN(setChoose='Validation', data=self.parentW.dataFor[self.senderName])

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

                    self.mj = Judgement.myJudge(self.parentW.trann.data.yClassDic,
                                                self.parentW.trann.getAccuratePredictResult().argmax(1),
                                                self.parentW.trann.data.DataValY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100,))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)

                    ########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.trann.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)



                elif self.dataSetName == 'Test':
                    try:
                        self.parentW.trann.runTraNN(setChoose='Test', data=self.parentW.dataFor[self.senderName])

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

                    self.mj = Judgement.myJudge(self.parentW.trann.data.yClassDic,
                                                self.parentW.trann.getAccuratePredictResult().argmax(1),
                                                self.parentW.trann.data.DataTestY.argmax(1))

                    self.mj.plotConfuseMatrix()
                    self.accuracy = self.mj.getAccuracy()
                    self.tpfptnfn = self.mj.getTPTNFPFN()
                    self.Precision = self.mj.getPrecision()
                    self.Recall = self.mj.getRecall()
                    self.f1Score = self.mj.calculateF1()

                    picTitleLayout = QHBoxLayout()
                    pictureTitleLabel = QLabel('混淆矩阵')
                    pictureTitleLabel.setFont(QFont('微软雅黑', 16))
                    picTitleLayout.addStretch(1)
                    picTitleLayout.addWidget(pictureTitleLabel)
                    picTitleLayout.addStretch(1)

                    picturelayout = QHBoxLayout()

                    self.confusionMatrixPicture = QLabel()
                    self.confusionMatrixPicture.resize(self.wlength * 0.8, 0.7 * self.whigh * 0.8)
                    scalePic = QPixmap('confusionMatrix.png')
                    # scalePic = scalePic.scaled(self.confusionMatrixPicture.size())
                    self.confusionMatrixPicture.setPixmap(scalePic)
                    self.confusionMatrixPicture.setScaledContents(True)
                    picturelayout.addStretch(1)
                    picturelayout.addWidget(self.confusionMatrixPicture)
                    picturelayout.addStretch(1)

                    acLayout = QHBoxLayout()
                    acLayout.addStretch(1)
                    Label = QLabel('Accuracy:')
                    Label.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(Label)
                    self.acLabel = QLabel('%.2f%%' % (self.accuracy * 100,))
                    self.acLabel.setFont(QFont('微软雅黑', 16))
                    acLayout.addWidget(self.acLabel)
                    acLayout.addStretch(1)

                    ########################### judge factors on different class #####################

                    self.judgeFactorShowListWidget = QListWidget()
                    # print(self.senderName)
                    # print(self.featureNum)
                    itemPattern = showJudgeFactorItem(self.makeListFirstLine())
                    item = QListWidgetItem(self.judgeFactorShowListWidget)
                    item.setSizeHint(itemPattern.sizeHint())
                    self.judgeFactorShowListWidget.addItem(item)
                    self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.labelDic = {v: k for k, v in self.parentW.trann.data.yClassDic.items()}
                    self.classNum = len(self.labelDic)

                    for i in range(self.classNum):
                        content = []
                        content.append('%-15s' % self.labelDic[i])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TruePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalsePositive'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['TrueNegative'])
                        content.append('%-15d' % self.tpfptnfn[self.labelDic[i]]['FalseNegative'])

                        content.append('%-15f' % self.Precision[self.labelDic[i]])

                        content.append('%-15f' % self.Recall[self.labelDic[i]])

                        content.append('%-15f' % self.f1Score[self.labelDic[i]])
                        # print(content)
                        # print(len(str(self.parentW.trann.getPredictResult()[i, :])))

                        itemPattern = showJudgeFactorItem(content)
                        item = QListWidgetItem(self.judgeFactorShowListWidget)
                        item.setSizeHint(itemPattern.sizeHint())
                        self.judgeFactorShowListWidget.addItem(item)
                        self.judgeFactorShowListWidget.setItemWidget(item, itemPattern)

                    self.judgeFactorShowListWidget.resize(self.judgeFactorShowListWidget.sizeHint())

                    layout.addStretch(1)
                    layout.addLayout(picTitleLayout)
                    layout.addLayout(picturelayout)
                    layout.addStretch(1)
                    layout.addLayout(acLayout)
                    layout.addStretch(1)
                    layout.addWidget(self.judgeFactorShowListWidget)
                    layout.addStretch(1)

        self.setLayout(layout)
        self.setWindowTitle(self.Title)
        self.setGeometry(500, 125, self.wlength, self.whigh)
        self.show()


    def makeListFirstLine(self):
        firstLine = list()
        firstLine.append('%-15s' % 'Label')

        firstLine.append('%-15s' % ('TruePositive', ))

        firstLine.append('%-15s' % 'FalsePositive')

        firstLine.append('%-15s' % 'TrueNegative')

        firstLine.append('%-15s' % 'FalseNegative')

        firstLine.append('%-15s' % 'Precision Rate')

        firstLine.append('%-15s' % 'Recall Rate')

        firstLine.append('%-15s' % 'F1 Score')

        # print(firstLine)
        return firstLine