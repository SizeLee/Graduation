####before training start, all the parameters and data should be check suitable by the training widget caller.

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QMessageBox, QProgressBar)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import pyqtSignal
from MyCombCNNPack import myCombineCNN
import re, threading, time

class trainningWidget(QWidget):
    def __init__(self, Title, parentW, senderName):
        super().__init__()
        self.Title = Title
        self.parentW = parentW
        self.senderName = senderName
        self.wlength = 900
        self.whigh = 700
        self.trainingTimes = 1600
        self.trainingRate = 0.2
        self.maxInt = 2147483647
        self.threadRunPermission = [True]
        self.listenProgressPermission = [True]
        self.trainingPicAccessLock = threading.Lock()

        self.initUI()
        self.initConnect()

    def closeEvent(self, QCloseEvent):
        self.threadRunPermission[0] = False
        self.listenProgressPermission[0] = False

        scalePic = QPixmap('start.jpg')
        scalePic = scalePic.scaled(self.trainingCostPicture.size())
        # self.trainingCostPicture.setPixmap(scalePic)
        self.trainingPicAccessLock.acquire()
        scalePic.save('TrainingCost.png')
        self.trainingPicAccessLock.release()

        if self.senderName == 'New':
            self.parentW.trainingW = None
        elif self.senderName == 'Tra':
            self.parentW.trainingWT = None


    def initUI(self):
        layout = QVBoxLayout()

        picTitleLayout = QHBoxLayout()
        pictureTitleLabel = QLabel('训练代价变化图')
        pictureTitleLabel.setFont(QFont('微软雅黑', 16))
        picTitleLayout.addStretch(1)
        picTitleLayout.addWidget(pictureTitleLabel)
        picTitleLayout.addStretch(1)

        picturelayout = QHBoxLayout()

        self.trainingCostPicture = QLabel()
        self.trainingCostPicture.resize(self.wlength, 0.625 * self.whigh)
        scalePic = QPixmap('start.jpg')
        scalePic = scalePic.scaled(self.trainingCostPicture.size())
        self.trainingCostPicture.setPixmap(scalePic)
        self.trainingCostPicture.setScaledContents(True)
        picturelayout.addStretch(1)
        picturelayout.addWidget(self.trainingCostPicture)
        picturelayout.addStretch(1)

        pBarLayout = QHBoxLayout()
        labelpb = QLabel('学习进度:')
        labelpb.setFont(QFont('微软雅黑', 16))
        self.progressBar = QLabel()
        self.progressBar.setFont(QFont('微软雅黑', 16))
        # self.progressBar.resize((self.wlength - 200), 25)
        self.progressBar.setText('%d%%' % 0)
        pBarLayout.addStretch(1)
        pBarLayout.addWidget(labelpb)
        pBarLayout.addWidget(self.progressBar)
        pBarLayout.addStretch(1)

        buttonLayout = QHBoxLayout()
        label1 = QLabel('训练次数:')
        label1.setFont(QFont('微软雅黑', 16))
        self.setTraingingTimes = QLineEdit(str(self.trainingTimes))
        self.setTraingingTimes.setFont(QFont('微软雅黑', 16))
        label2 = QLabel('学习速率:')
        label2.setFont(QFont('微软雅黑', 16))
        self.setTrainingRate = QLineEdit(str(self.trainingRate))
        self.setTrainingRate.setFont(QFont('微软雅黑', 16))
        self.button = QPushButton('Start')
        self.button.setFont(QFont('微软雅黑', 16))
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(label1)
        buttonLayout.addWidget(self.setTraingingTimes)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(label2)
        buttonLayout.addWidget(self.setTrainingRate)
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.button)
        buttonLayout.addStretch(1)

        layout.addStretch(1)
        layout.addLayout(picTitleLayout)
        layout.addLayout(picturelayout)
        layout.addStretch(1)
        layout.addLayout(pBarLayout)
        layout.addStretch(1)
        layout.addLayout(buttonLayout)
        layout.addStretch(1)

        self.setLayout(layout)
        self.setWindowTitle(self.Title)
        self.setGeometry(500, 200, self.wlength, self.whigh)
        self.show()

    def initConnect(self):
        self.button.clicked.connect(self.training)
        # self.progressBar.valueChanged.connect(self.progressChange)

    def progressChange(self):
        while self.listenProgressPermission[0]:
            progress = int(self.parentW.mcbcnn.getTrainingProgress() * 100 + 0.5)
            # print(progress)
            self.progressBar.setText('%d%%' % progress)
            self.trainingPicAccessLock.acquire()
            self.trainingCostPicture.setPixmap(QPixmap('TrainingCost.png'))
            self.trainingPicAccessLock.release()
            if progress >= 100:
                self.button.setText('Finished')
                break
            time.sleep(1)


    def training(self):
        if self.sender().text() == 'Start':
            errorMessage = ''
            if not self.isInteger(self.setTraingingTimes.text()):
                errorMessage = errorMessage + '训练次数无效输入\n'
            elif int(self.setTraingingTimes.text()) <= 0 or int(self.setTraingingTimes.text()) >= self.maxInt:
                errorMessage = errorMessage + '训练次数输入范围错误\n'

            if not self.isNumber(self.setTrainingRate.text()):
                errorMessage = errorMessage + '学习速率无效输入\n'
            elif float(self.setTrainingRate.text()) <= 0.:
                errorMessage = errorMessage + '学习速率输入范围错误\n'

            if errorMessage != '':
                errorMessage = errorMessage + '请重新输入参数'
                reply = QMessageBox.information(self, '输入错误', errorMessage,
                                                QMessageBox.Yes, QMessageBox.Yes)

                self.setTraingingTimes.setText(str(self.trainingTimes))
                self.setTrainingRate.setText(str(self.trainingRate))
                return

            self.trainingTimes = int(self.setTraingingTimes.text())
            self.trainingRate = float(self.setTrainingRate.text())

            self.threadRunPermission[0] = True
            self.listenProgressPermission[0] = True
            self.sender().setText('Stop')
            if self.senderName == 'New':
                self.parentW.mcbcnn = myCombineCNN.myCombineCNN(self.parentW.dataFor[self.senderName],
                                                                self.parentW.combineNumConv,
                                                                self.parentW.convCoreNum,
                                                                self.parentW.combineNumPooling)

                trainingThread = threading.Thread(target=self.parentW.mcbcnn.trainCNN,
                                                args=(self.trainingTimes, self.trainingRate,
                                                      self.threadRunPermission, self.trainingPicAccessLock))
                trainingThread.setDaemon(True)
                trainingThread.start()

                listenProgressThread = threading.Thread(target=self.progressChange)
                listenProgressThread.setDaemon(True)
                listenProgressThread.start()

            elif self.senderName == 'Tra':
                pass

        elif self.sender().text() == 'Stop':
            self.threadRunPermission[0] = False
            self.listenProgressPermission[0] = False
            self.sender().setText('Start')
            scalePic = QPixmap('start.jpg')
            scalePic = scalePic.scaled(self.trainingCostPicture.size())
            # self.trainingCostPicture.setPixmap(scalePic)
            self.trainingPicAccessLock.acquire()
            scalePic.save('TrainingCost.png')
            self.trainingPicAccessLock.release()

        elif self.sender().text() == 'Finished':
            self.progressBar.setText('%d%%' % 0)
            self.button.setText('Start')
            scalePic = QPixmap('start.jpg')
            scalePic = scalePic.scaled(self.trainingCostPicture.size())
            self.trainingCostPicture.setPixmap(scalePic)
            self.trainingPicAccessLock.acquire()
            scalePic.save('TrainingCost.png')
            self.trainingPicAccessLock.release()

    def threadFinishWork(self):
        self.button.setText('Start')

    def isNumber(self, str):
        regex = re.compile(r'^[-+]?[0-9]+\.?[0-9]*$')
        result = regex.match(str)

        return result

    def isInteger(self, str):
        regex = re.compile('^[-+]?[0-9]+$')
        result = regex.match(str)

        return result

    # class TrainingThread(QThread):
    #     def __init__(self, mcbcnn):
    #         super.__init__()###############todo#########3
    #         self.mcbcnn = mcbcnn


