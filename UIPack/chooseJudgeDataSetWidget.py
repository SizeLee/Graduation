from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QProgressBar, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import pyqtSignal
from MyCombCNNPack import myCombineCNN, traditionalNN, myException, Judgement
import re, threading, time
from UIPack import showJudgeWidgets


class chooseJudgeDataSetWidget(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.wlength = 800
        self.whigh = 400

        self.initUI()
        self.initConnect()

    def initUI(self):
        layout = QHBoxLayout()
        self.btnTrain = QPushButton('Train Data Set')
        self.btnTrain.setFont(QFont('微软雅黑', 16))

        self.btnVal = QPushButton('Validation Data Set')
        self.btnVal.setFont(QFont('微软雅黑', 16))

        self.btnTest = QPushButton('Test Data Set')
        self.btnTest.setFont(QFont('微软雅黑', 16))

        layout.addStretch(1)
        layout.addWidget(self.btnTrain)
        layout.addStretch(1)
        layout.addWidget(self.btnVal)
        layout.addStretch(1)
        layout.addWidget(self.btnTest)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setWindowTitle(self.Title)
        if self.senderName == 'New':
            self.setGeometry(500, 200, self.wlength, self.whigh)

        elif self.senderName == 'Tra':
            self.setGeometry(500, 600, self.wlength, self.whigh)

        self.show()


    def initConnect(self):
        self.btnTrain.clicked.connect(self.showJudge)
        self.btnVal.clicked.connect(self.showJudge)
        self.btnTest.clicked.connect(self.showJudge)


    def showJudge(self):
        if self.sender() is self.btnTrain:
            self.showJudgeWin = showJudgeWidgets.judgeWidget('Judgement based on Training Data Set', self.parentW,
                                                             self.senderName, 'Train')

        elif self.sender() is self.btnVal:
            self.showJudgeWin = showJudgeWidgets.judgeWidget('Judgement based on Validation Data Set', self.parentW,
                                                             self.senderName, 'Validation')

        elif self.sender() is self.btnTest:
            self.showJudgeWin = showJudgeWidgets.judgeWidget('Judgement based on Test Data Set', self.parentW,
                                                             self.senderName, 'Test')

        return