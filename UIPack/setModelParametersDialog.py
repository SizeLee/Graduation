from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox)
from PyQt5.QtGui import QFont
import re
import myLoadData

class setLossParameterDialog(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.maxInt = 2147483647
        self.initUI()
        self.initConnect()

    def initUI(self):
        sMPLayout = QVBoxLayout()
        sMPLayout.addStretch(2)

        if self.senderName == 'New':
            setCombineNumConvLabel = QLabel('卷积层特征组合大小(卷积核大小):')
            setCombineNumConvLabel.setFont(QFont('微软雅黑', 16))
            self.setCombineNumConvEdit = QLineEdit('%s' % str(self.parentW.combineNumConv))
            self.setCombineNumConvEdit.setFont(QFont('微软雅黑', 16))
            self.setCombineNumConvEdit.resize(self.setCombineNumConvEdit.sizeHint())

            setCombineNumCovLayout = QHBoxLayout()
            setCombineNumCovLayout.addStretch(1)
            setCombineNumCovLayout.addWidget(setCombineNumConvLabel)
            setCombineNumCovLayout.addWidget(self.setCombineNumConvEdit)
            setCombineNumCovLayout.addStretch(1)

            setConvCoreNumLabel = QLabel('                                  卷积核数量:')
            setConvCoreNumLabel.setFont(QFont('微软雅黑', 16))
            self.setConvCoreNumEdit = QLineEdit('%s' % str(self.parentW.convCoreNum))
            self.setConvCoreNumEdit.setFont(QFont('微软雅黑', 16))

            setConvCoreNumLayout = QHBoxLayout()
            setConvCoreNumLayout.addStretch(1)
            setConvCoreNumLayout.addWidget(setConvCoreNumLabel)
            setConvCoreNumLayout.addWidget(self.setConvCoreNumEdit)
            setConvCoreNumLayout.addStretch(1)

            setCombineNumPoolingLabel = QLabel('池化层特征组合大小(池化核大小):')
            setCombineNumPoolingLabel.setFont(QFont('微软雅黑', 16))
            self.setCombineNumPoolingEdit = QLineEdit('%s' % str(self.parentW.combineNumPooling))
            self.setCombineNumPoolingEdit.setFont(QFont('微软雅黑', 16))

            setCombineNumPoolingLayout = QHBoxLayout()
            setCombineNumPoolingLayout.addStretch(1)
            setCombineNumPoolingLayout.addWidget(setCombineNumPoolingLabel)
            setCombineNumPoolingLayout.addWidget(self.setCombineNumPoolingEdit)
            setCombineNumPoolingLayout.addStretch(1)

            sMPLayout.addLayout(setCombineNumCovLayout)
            sMPLayout.addStretch(2)
            sMPLayout.addLayout(setConvCoreNumLayout)
            sMPLayout.addStretch(2)
            sMPLayout.addLayout(setCombineNumPoolingLayout)
            sMPLayout.addStretch(2)

            self.resize(700, 400)


        elif self.senderName == 'Tra':
            setFullConnectOutInRateLabel = QLabel('全连接(隐层/输入层)大小比例:')
            setFullConnectOutInRateLabel.setFont(QFont('微软雅黑', 16))
            self.setFullConnectOutInRateEdit = QLineEdit('%s' % str(self.parentW.fullConnectOutInRate))
            self.setFullConnectOutInRateEdit.setFont(QFont('微软雅黑', 16))

            setFullConnectOutInRateLayout = QHBoxLayout()
            setFullConnectOutInRateLayout.addStretch(1)
            setFullConnectOutInRateLayout.addWidget(setFullConnectOutInRateLabel)
            setFullConnectOutInRateLayout.addWidget(self.setFullConnectOutInRateEdit)
            setFullConnectOutInRateLayout.addStretch(1)

            sMPLayout.addLayout(setFullConnectOutInRateLayout)
            sMPLayout.addStretch(2)

            self.resize(700, 300)

        self.confirmButton = QPushButton('确定')
        self.confirmButton.setFont(QFont('微软雅黑', 16))
        self.cancelButton = QPushButton('取消')
        self.cancelButton.setFont(QFont('微软雅黑', 16))

        confirmLayout = QHBoxLayout()
        confirmLayout. addStretch(2)
        confirmLayout.addWidget(self.confirmButton)
        confirmLayout.addStretch(1)
        confirmLayout.addWidget(self.cancelButton)
        confirmLayout.addStretch(1)

        sMPLayout.addLayout(confirmLayout)
        sMPLayout.addStretch(1)

        self.setLayout(sMPLayout)
        self.setWindowTitle(self.Title)
        self.move(500, 350)
        self.show()


    def initConnect(self):
        self.cancelButton.clicked.connect(self.close)
        self.confirmButton.clicked.connect(self.confirmParameters)

    def confirmParameters(self):
        if self.senderName == 'New':
            errorMessage = ''
            if not self.isInteger(self.setCombineNumConvEdit.text()):
                errorMessage = errorMessage + '卷积层特征组合大小(卷积核大小)无效输入\n'
            elif int(self.setCombineNumConvEdit.text()) <= 0 or int(self.setCombineNumConvEdit.text()) >= self.maxInt:
                errorMessage = errorMessage + '卷积层特征组合大小(卷积核大小)输入范围错误\n'

            if not self.isInteger(self.setConvCoreNumEdit.text()):
                errorMessage = errorMessage + '卷积核数量无效输入\n'
            elif int(self.setConvCoreNumEdit.text()) <= 0 or int(self.setConvCoreNumEdit.text()) >= self.maxInt:
                errorMessage = errorMessage + '卷积核数量输入范围错误\n'

            if not self.isInteger(self.setCombineNumPoolingEdit.text()):
                errorMessage = errorMessage + '池化层特征组合大小(池化核大小)无效输入\n'
            elif int(self.setCombineNumPoolingEdit.text()) <= 0 or int(self.setCombineNumPoolingEdit.text()) >= self.maxInt:
                errorMessage = errorMessage + '池化层特征组合大小(池化核大小)输入范围错误\n'

            if errorMessage != '':
                errorMessage = errorMessage + '请重新输入参数'
                reply = QMessageBox.information(self, '输入错误', errorMessage,
                                                QMessageBox.Yes, QMessageBox.Yes)

                self.setCombineNumConvEdit.setText(str(self.parentW.combineNumConv))
                self.setConvCoreNumEdit.setText(str(self.parentW.convCoreNum))
                self.setCombineNumPoolingEdit.setText(str(self.parentW.combineNumPooling))
                return

            else:
                self.parentW.combineNumConv = int(self.setCombineNumConvEdit.text())
                self.parentW.convCoreNum = int(self.setConvCoreNumEdit.text())
                self.parentW.combineNumPooling = int(self.setCombineNumPoolingEdit.text())


        elif self.senderName == 'Tra':
            errorMessage = ''
            if not self.isNumber(self.setFullConnectOutInRateEdit.text()):
                errorMessage = errorMessage + '全连接(隐层/输入层)大小比例无效输入\n'
            elif float(self.setFullConnectOutInRateEdit.text()) <= 0.:
                errorMessage = errorMessage + '全连接(隐层/输入层)大小比例输入范围错误\n'

            if errorMessage != '':
                errorMessage = errorMessage + '请重新输入参数'
                reply = QMessageBox.information(self, '输入错误', errorMessage,
                                                QMessageBox.Yes, QMessageBox.Yes)

                self.setFullConnectOutInRateEdit.setText(str(self.parentW.fullConnectOutInRate))
                return

            else:
                self.parentW.fullConnectOutInRate = float(self.setFullConnectOutInRateEdit.text())


        reply = QMessageBox.information(self, 'Message', "Parameters' saved successfully",
                                         QMessageBox.Yes, QMessageBox.Yes)
        self.close()
        return


    def isNumber(self, str):
        regex = re.compile(r'^[-+]?[0-9]+\.?[0-9]*$')
        result = regex.match(str)

        return result

    def isInteger(self, str):
        regex = re.compile('^[-+]?[0-9]+$')
        result = regex.match(str)

        return result
