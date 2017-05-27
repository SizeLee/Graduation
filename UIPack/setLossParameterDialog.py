from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import re
import myLoadData

class setLossParameterDialog(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.initUI()
        self.initConnect()

    def initUI(self):
        # print(self.parentW.presentDataName.text())
        # print(self.sender() is self.parentW.dataLossSimulateSettingButton)

        setLossRateLabel = QLabel('       缺失率:')
        setLossRateLabel.setFont(QFont('微软雅黑', 16))
        self.setLossRateEdit = QLineEdit('%s' % str(self.parentW.dataLossRate[self.senderName]))
        self.setLossRateEdit.setFont(QFont('微软雅黑', 16))

        setLossRateLayout = QHBoxLayout()
        setLossRateLayout.addStretch(1)
        setLossRateLayout.addWidget(setLossRateLabel)
        setLossRateLayout.addWidget(self.setLossRateEdit)
        setLossRateLayout.addStretch(1)

        setLossValueLabel = QLabel('缺失标示值:')
        setLossValueLabel.setFont(QFont('微软雅黑', 16))
        self.setLossValueEdit = QLineEdit('%s' % str(self.parentW.dataSetLossValue[self.senderName]))
        self.setLossValueEdit.setFont(QFont('微软雅黑', 16))

        setLossValueLayout = QHBoxLayout()
        setLossValueLayout.addStretch(1)
        setLossValueLayout.addWidget(setLossValueLabel)
        setLossValueLayout.addWidget(self.setLossValueEdit)
        setLossValueLayout.addStretch(1)

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

        sLPLayout =QVBoxLayout()
        sLPLayout.addStretch(2)
        sLPLayout.addLayout(setLossRateLayout)
        sLPLayout.addStretch(2)
        sLPLayout.addLayout(setLossValueLayout)
        sLPLayout.addStretch(2)
        sLPLayout.addLayout(confirmLayout)
        sLPLayout.addStretch(1)

        self.setLayout(sLPLayout)
        self.setWindowTitle(self.Title)
        self.setGeometry(500, 350, 500, 400)
        self.show()


    def initConnect(self):
        self.cancelButton.clicked.connect(self.close)
        self.confirmButton.clicked.connect(self.confirmParameters)


    def keyPressEvent(self, QKeyEvent):
        # print(QKeyEvent.key())
        # print(QtCore.Qt.Key_Enter)
        if QKeyEvent.key() == QtCore.Qt.Key_Enter or QKeyEvent.key() == QtCore.Qt.Key_Enter - 1:
            self.confirmParameters()


    def confirmParameters(self):
        errorMessage = ''
        if not self.isNumber(self.setLossRateEdit.text()):
            errorMessage = errorMessage + '缺失率无效输入\n'
        elif float(self.setLossRateEdit.text()) > 1. or float(self.setLossRateEdit.text()) < 0.:
            errorMessage = errorMessage + '缺失率输入范围错误\n'

        if not self.isNumber(self.setLossValueEdit.text()):
            errorMessage = errorMessage + '缺失标示值无效输入\n'

        if errorMessage != '':
            errorMessage = errorMessage + '请重新输入参数'
            reply = QMessageBox.information(self, '输入错误', errorMessage,
                                            QMessageBox.Yes, QMessageBox.Yes)

            self.setLossRateEdit.setText(str(self.parentW.dataLossRate[self.senderName]))
            self.setLossValueEdit.setText(str(self.parentW.dataSetLossValue[self.senderName]))
            return

        else:
            self.parentW.dataLossRate[self.senderName] = float(self.setLossRateEdit.text())
            self.parentW.dataSetLossValue[self.senderName] = float(self.setLossValueEdit.text())
            if self.parentW.fname[self.senderName] is not None:
                try:
                    self.parentW.dataFor[self.senderName] = myLoadData.loadData(self.parentW.fname[self.senderName],
                                                                            self.parentW.dataLossRate[self.senderName],
                                                                            self.parentW.dataSetLossValue[self.senderName])

                except FileNotFoundError as e:
                    reply = QMessageBox.information(self, 'Message', "Data file doesn't exist, parameters' saved",
                                                    QMessageBox.Yes, QMessageBox.Yes)
                    # print(self.parentW.dataFor[self.senderName].DataTrainX)
                    self.close()
                    return

            # if self.parentW.dataFor['New'] is not None:
            #     print(self.parentW.dataFor['New'].DataTrainX, '\n', self.parentW.dataFor['New'].DataTrainY)
            # else:
            #     print(self.parentW.dataFor['New'])
            #
            # if self.parentW.dataFor['Tra'] is not None:
            #     print(self.parentW.dataFor['Tra'].DataTrainX, '\n', self.parentW.dataFor['Tra'].DataTrainY)
            # else:
            #     print(self.parentW.dataFor['Tra'])

            reply = QMessageBox.information(self, 'Message', "Parameters' saved successfully",
                                            QMessageBox.Yes, QMessageBox.Yes)
            self.close()
            return


    def isNumber(self, str):
        regex = re.compile(r'^[-+]?[0-9]+\.?[0-9]*$')
        result = regex.match(str)

        return result
