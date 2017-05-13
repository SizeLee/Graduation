import sys
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame,
    QSplitter, QStyleFactory, QApplication, QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
import myLoadData
from UIPack import setLossParameterDialog, showDataWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowLength = 1250
        self.windowHigh = 900

        self.fname = dict()
        self.fname['New'] = None
        self.fname['Tra'] = None

        self.dataLossRate = dict()
        self.dataSetLossValue = dict()
        self.dataFor = dict()

        self.dataFor['New'] = None
        self.dataLossRate['New'] = 0.
        self.dataSetLossValue['New'] = 0.

        self.dataFor['Tra'] = None
        self.dataLossRate['Tra'] = 0.
        self.dataSetLossValue['Tra'] = 0.


        self.initUI()
        self.initConnect()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        ####### data module #######
        dataModule = QVBoxLayout()

        self.dataFileChooseButton = QPushButton('选择数据')
        self.dataFileChooseButton.setFont(QFont('微软雅黑', 16))
        self.dataLossSimulateSettingButton = QPushButton('设置数据缺失参数')
        self.dataLossSimulateSettingButton.setFont(QFont('微软雅黑', 16))
        self.dataShowButton = QPushButton('展示数据')
        self.dataShowButton.setFont(QFont('微软雅黑', 16))

        label = QLabel('Present Data:')
        label.setFont(QFont('微软雅黑', 16))
        self.presentDataName = QLabel('None')
        self.presentDataName.setFont(QFont('微软雅黑', 16))
        labelbox = QVBoxLayout()
        labelbox.addWidget(label)
        labelbox.addWidget(self.presentDataName)

        dataModule.addStretch(1)
        dataModule.addLayout(labelbox)
        dataModule.addStretch(1)
        dataModule.addWidget(self.dataFileChooseButton)
        dataModule.addStretch(1)
        dataModule.addWidget(self.dataLossSimulateSettingButton)
        dataModule.addStretch(1)
        dataModule.addWidget(self.dataShowButton)
        dataModule.addStretch(1)


        ###### training module ########
        trainingModule = QVBoxLayout()

        self.setModelParametersButton = QPushButton('Model Parameters')
        self.setModelParametersButton.setFont(QFont('微软雅黑', 16))
        # self.setTrainingParametersButton = QPushButton('Trainning Parameters')
        # self.setTrainingParametersButton.setFont(QFont('微软雅黑', 16))
        self.trainingButton = QPushButton('Training')
        self.trainingButton.setFont(QFont('微软雅黑', 16))
        self.saveModelButton = QPushButton('Save Model')
        self.saveModelButton.setFont(QFont('微软雅黑', 16))
        self.loadModelButton = QPushButton('Load Model')
        self.loadModelButton.setFont(QFont('微软雅黑', 16))

        label = QLabel('Present Model:')
        label.setFont(QFont('微软雅黑', 16))
        self.presentModelName = QLabel('None')
        self.presentModelName.setFont(QFont('微软雅黑', 16))
        labelbox = QVBoxLayout()
        labelbox.addWidget(label)
        labelbox.addWidget(self.presentModelName)

        trainingModule.addStretch(1)
        trainingModule.addLayout(labelbox)
        trainingModule.addStretch(1)
        trainingModule.addWidget(self.setModelParametersButton)
        trainingModule.addStretch(1)
        trainingModule.addWidget(self.trainingButton)
        trainingModule.addStretch(1)
        trainingModule.addWidget(self.saveModelButton)
        trainingModule.addStretch(1)
        trainingModule.addWidget(self.loadModelButton)
        trainingModule.addStretch(1)

        ############## new cnn result show ######
        resultShowModule = QVBoxLayout()

        self.showResultButton = QPushButton('分类结果展示')
        self.showResultButton.setFont(QFont('微软雅黑', 16))
        self.judgeResultButton = QPushButton('分类结果评估')
        self.judgeResultButton.setFont(QFont('微软雅黑', 16))

        resultShowModule.addWidget(self.showResultButton)
        resultShowModule.addWidget(self.judgeResultButton)

        #################  new algorithm ui ##########
        hboxTop = QHBoxLayout()
        hboxTop.addStretch(1)

        mcnnLabel = QLabel('Combine-CNN:')
        mcnnLabel.setFont(QFont('微软雅黑', 24, QFont.Bold))
        hboxTop.addWidget(mcnnLabel)

        hboxTop.addStretch(1)

        hboxTop.addLayout(dataModule)

        hboxTop.addStretch(1)

        hboxTop.addLayout(trainingModule)

        hboxTop.addStretch(1)

        hboxTop.addLayout(resultShowModule)

        hboxTop.addStretch(1)

        #########traditional data module##########
        dataModuleT = QVBoxLayout()

        self.dataFileChooseButtonT = QPushButton('选择数据')
        self.dataFileChooseButtonT.setFont(QFont('微软雅黑', 16))
        self.dataLossSimulateSettingButtonT = QPushButton('设置数据缺失参数')
        self.dataLossSimulateSettingButtonT.setFont(QFont('微软雅黑', 16))
        self.dataPreProcessButtonT = QPushButton('数据预处理')
        self.dataPreProcessButtonT.setFont(QFont('微软雅黑', 16))
        self.dataShowButtonT = QPushButton('展示数据')
        self.dataShowButtonT.setFont(QFont('微软雅黑', 16))

        label = QLabel('Present Data:')
        label.setFont(QFont('微软雅黑', 16))
        self.presentDataNameT = QLabel('None')
        self.presentDataNameT.setFont(QFont('微软雅黑', 16))
        labelbox = QVBoxLayout()
        labelbox.addWidget(label)
        labelbox.addWidget(self.presentDataNameT)

        dataModuleT.addStretch(1)
        dataModuleT.addLayout(labelbox)
        dataModuleT.addStretch(1)
        dataModuleT.addWidget(self.dataFileChooseButtonT)
        dataModuleT.addStretch(1)
        dataModuleT.addWidget(self.dataLossSimulateSettingButtonT)
        dataModuleT.addStretch(1)
        dataModuleT.addWidget(self.dataPreProcessButtonT)
        dataModuleT.addStretch(1)
        dataModuleT.addWidget(self.dataShowButtonT)
        dataModuleT.addStretch(1)

        ###### training module ########
        trainingModuleT = QVBoxLayout()

        self.setModelParametersButtonT = QPushButton('Model Parameters')
        self.setModelParametersButtonT.setFont(QFont('微软雅黑', 16))
        self.trainingButtonT = QPushButton('Training')
        self.trainingButtonT.setFont(QFont('微软雅黑', 16))
        self.saveModelButtonT = QPushButton('Save Model')
        self.saveModelButtonT.setFont(QFont('微软雅黑', 16))
        self.loadModelButtonT = QPushButton('Load Model')
        self.loadModelButtonT.setFont(QFont('微软雅黑', 16))

        label = QLabel('Present Model:')
        label.setFont(QFont('微软雅黑', 16))
        self.presentModelNameT = QLabel('None')
        self.presentModelNameT.setFont(QFont('微软雅黑', 16))
        labelbox = QVBoxLayout()
        labelbox.addWidget(label)
        labelbox.addWidget(self.presentModelNameT)

        trainingModuleT.addStretch(1)
        trainingModuleT.addLayout(labelbox)
        trainingModuleT.addStretch(1)
        trainingModuleT.addWidget(self.setModelParametersButtonT)
        trainingModuleT.addStretch(1)
        trainingModuleT.addWidget(self.trainingButtonT)
        trainingModuleT.addStretch(1)
        trainingModuleT.addWidget(self.saveModelButtonT)
        trainingModuleT.addStretch(1)
        trainingModuleT.addWidget(self.loadModelButtonT)
        trainingModuleT.addStretch(1)

        ############## traditional nn result show ######
        resultShowModuleT = QVBoxLayout()

        self.showResultButtonT = QPushButton('分类结果展示')
        self.showResultButtonT.setFont(QFont('微软雅黑', 16))
        self.judgeResultButtonT = QPushButton('分类结果评估')
        self.judgeResultButtonT.setFont(QFont('微软雅黑', 16))

        resultShowModuleT.addWidget(self.showResultButtonT)
        resultShowModuleT.addWidget(self.judgeResultButtonT)

        ####### traditional algorithm #########
        hboxBottom = QHBoxLayout(self)
        hboxBottom.addStretch(1)

        traditionNNLabel = QLabel('Traditional NN:')
        traditionNNLabel.setFont(QFont('微软雅黑', 24, QFont.Bold))
        hboxBottom.addWidget(traditionNNLabel)

        hboxBottom.addStretch(1)

        hboxBottom.addLayout(dataModuleT)

        hboxBottom.addStretch(1)

        hboxBottom.addLayout(trainingModuleT)

        hboxBottom.addStretch(1)

        hboxBottom.addLayout(resultShowModuleT)

        hboxBottom.addStretch(1)

        ########## whole frame layout ########
        splitterLine = QLabel(self)
        splitterLine.setFont(QFont('Times', 1))
        col = QColor(0, 0, 0)
        splitterLine.setStyleSheet("QWidget { background-color: %s }" % col.name())
        splitterLine.resize(splitterLine.sizeHint())

        vbox = QVBoxLayout()
        vbox.addLayout(hboxTop)
        # vbox.addWidget(QLabel(str('_'*int(self.width()/3))))
        vbox.addWidget(splitterLine)
        vbox.addLayout(hboxBottom)

        mainWidget = QWidget()
        mainWidget.setLayout(vbox)

        self.setCentralWidget(mainWidget)

        self.setGeometry(350, 100, self.windowLength, self.windowHigh)
        self.setWindowTitle('适用于有缺失值数据集的神经网络系统')
        self.show()

    def initConnect(self):

        self.dataFileChooseButton.clicked.connect(self.chooseData)
        self.dataFileChooseButtonT.clicked.connect(self.chooseData)
        self.dataLossSimulateSettingButton.clicked.connect(self.setLossParameter)
        self.dataLossSimulateSettingButtonT.clicked.connect(self.setLossParameter)
        self.dataShowButton.clicked.connect(self.showData)
        self.dataShowButtonT.clicked.connect(self.showData)
        self.dataPreProcessButtonT.clicked.connect(self.preProcess)


    def chooseData(self):
        if self.sender() is self.dataFileChooseButton:
            self.fname['New'], ok = QFileDialog.getOpenFileName(self, 'Open file', '..', 'Text files (*.txt)')
            if ok:
                dataname = self.fname['New'].split('/')[-1].split('.')[0]
                # print(dataname)
                self.presentDataName.setText(dataname)
                self.presentDataName.resize(self.presentDataName.sizeHint())
                self.loadData()

        elif self.sender() is self.dataFileChooseButtonT:
            self.fname['Tra'], ok = QFileDialog.getOpenFileName(self, 'Open file', '..', 'Text files (*.txt)')
            if ok:
                dataname = self.fname['Tra'].split('/')[-1].split('.')[0]
                # print(dataname)
                self.presentDataNameT.setText(dataname)
                self.presentDataNameT.resize(self.presentDataNameT.sizeHint())
                self.loadData()

        return


    def loadData(self):
        if self.sender() is self.dataFileChooseButton:
            try:
                self.dataFor['New'] = myLoadData.loadData(self.fname['New'], self.dataLossRate['New'], self.dataSetLossValue['New'])
                # print(self.dataFor['New'].DataTrainX, '\n', self.dataFor['New'].DataTrainY)

            except FileNotFoundError as e:
                reply = QMessageBox.question(self, 'Message', "Data file not exist",
                                             QMessageBox.Yes, QMessageBox.Yes)
                return

        elif self.sender() is self.dataFileChooseButtonT:
            try:
                self.dataFor['Tra'] = myLoadData.loadData(self.fname['Tra'], self.dataLossRate['Tra'], self.dataSetLossValue['Tra'])
                # print(self.dataFor['Tra'].DataTrainX, '\n', self.dataFor['Tra'].DataTrainY)

            except FileNotFoundError as e:
                reply = QMessageBox.question(self, 'Message', "Data file not exist",
                                             QMessageBox.Yes, QMessageBox.Yes)
                return

        return

    def setLossParameter(self):
        if self.sender() is self.dataLossSimulateSettingButton:
            self.setLPDialog = setLossParameterDialog.setLossParameterDialog('combine-CNN设置缺失参数', self, 'New')

        elif self.sender() is self.dataLossSimulateSettingButtonT:
            self.setLPDialog = setLossParameterDialog.setLossParameterDialog('traditional NN设置缺失参数', self, 'Tra')

        # print(self.dataLossRate)
        # print(self.dataSetLossValue)
        return

    def showData(self):
        if self.sender() is self.dataShowButton:
            # print(1)
            self.showDataW = showDataWidget.ShowDataWidget('combine-CNN数据展示', self, 'New')

        elif self.sender() is self.dataShowButtonT:
            # print(1)
            self.showDataW = showDataWidget.ShowDataWidget('traditional NN数据展示', self, 'Tra')

    def preProcess(self):
        if self.dataFor['Tra'] is None:
            reply = QMessageBox.question(self, '数据错误', '没有加载数据，无法预处理',
                                         QMessageBox.Yes, QMessageBox.Yes)
        else:
            self.dataFor['Tra'].MeanPreProcess()
            reply = QMessageBox.question(self, 'Message', 'PreProcess succeed!',
                                         QMessageBox.Yes, QMessageBox.Yes)

        return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = MyMainWindow()
    sys.exit(app.exec_())