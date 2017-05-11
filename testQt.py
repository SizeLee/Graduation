# import sys
# from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         textEdit = QTextEdit()
#         self.setCentralWidget(textEdit)
#
#         exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(self.close)
#
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exitAction)
#
#         toolbar = self.addToolBar('Exit')
#         toolbar.addAction(exitAction)
#
#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('Main window')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton,
#                              QHBoxLayout, QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle('Buttons')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QGridLayout,
#                              QPushButton, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         grid = QGridLayout()
#         self.setLayout(grid)
#
#         names = ['Cls', 'Bck', '', 'Close',
#                  '7', '8', '9', '/',
#                  '4', '5', '6', '*',
#                  '1', '2', '3', '-',
#                  '0', '.', '=', '+']
#
#         positions = [(i, j) for i in range(5) for j in range(4)]
#
#         for position, name in zip(positions, names):
#
#             if name == '':
#                 continue
#             button = QPushButton(name)
#             grid.addWidget(button, *position)
#
#         self.move(300, 150)
#         self.setWindowTitle('Calculator')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
#                              QTextEdit, QGridLayout, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         title = QLabel('Title')
#         author = QLabel('Author')
#         review = QLabel('Review')
#
#         titleEdit = QLineEdit()
#         authorEdit = QLineEdit()
#         reviewEdit = QTextEdit()
#
#         grid = QGridLayout()
#         grid.setSpacing(10)
#
#         grid.addWidget(title, 1, 0)
#         grid.addWidget(titleEdit, 1, 1)
#
#         grid.addWidget(author, 2, 0)
#         grid.addWidget(authorEdit, 2, 1)
#
#         grid.addWidget(review, 3, 0)
#         grid.addWidget(reviewEdit, 3, 1, 5, 1)
#
#         self.setLayout(grid)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('Review')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
#                              QVBoxLayout, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
#
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
#
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & slot')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import pyqtSignal, QObject
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
#
# class Communicate(QObject):
#     closeApp = pyqtSignal()
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Emit signal')
#         self.show()
#
#     def mousePressEvent(self, event):
#         self.c.closeApp.emit()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
#                              QInputDialog, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le = QLineEdit(self)
#         self.le.move(130, 22)
#
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Input dialog')
#         self.show()
#
#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'Input Dialog',
#                                         'Enter your name:')
#
#         if ok:
#             self.le.setText(str(text))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame,
#                              QColorDialog, QApplication)
# from PyQt5.QtGui import QColor
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         col = QColor(0, 0, 0)
#
#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
#
#         self.btn.clicked.connect(self.showDialog)
#
#         self.frm = QFrame(self)
#         self.frm.setStyleSheet("QWidget { background-color: %s }"
#                                % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)
#
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Color dialog')
#         self.show()
#
#     def showDialog(self):
#         col = QColorDialog.getColor()
#
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget { background-color: %s }"
#                                    % col.name())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
#                              QSizePolicy, QLabel, QFontDialog, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         vbox = QVBoxLayout()
#
#         btn = QPushButton('Dialog', self)
#         btn.setSizePolicy(QSizePolicy.Fixed,
#                           QSizePolicy.Fixed)
#
#         btn.move(20, 20)
#
#         vbox.addWidget(btn)
#
#         btn.clicked.connect(self.showDialog)
#
#         self.lbl = QLabel('Knowledge only matters', self)
#         self.lbl.move(130, 20)
#
#         vbox.addWidget(self.lbl)
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Font dialog')
#         self.show()
#
#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.lbl.setFont(font)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        saveFile = QAction('Save', self)
        saveFile.triggered.connect(self.saveFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        if fname[0]:
            # print(fname[0])
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def saveFile(self):
        fname, ok = QFileDialog.getSaveFileName(self, 'Save file', '.\\model.txt', 'Text files (*.txt)')
        if ok:
            with open(fname, 'w+') as f:
                f.write('234')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         cb = QCheckBox('Show title', self)
#         cb.move(20, 20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QCheckBox')
#         self.show()
#
#     def changeTitle(self, state):
#
#         if state == Qt.Checked:
#             self.setWindowTitle('QCheckBox')
#         else:
#             self.setWindowTitle('')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton,
#                              QFrame, QApplication)
# from PyQt5.QtGui import QColor
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.col = QColor(0, 0, 0)
#
#         redb = QPushButton('Red', self)
#         redb.setCheckable(True)
#         redb.move(10, 10)
#
#         redb.clicked[bool].connect(self.setColor)
#
#         greenb = QPushButton('Green', self)
#         greenb.setCheckable(True)
#         greenb.move(10, 60)
#
#         greenb.clicked[bool].connect(self.setColor)
#
#         blueb = QPushButton('Blue', self)
#         blueb.setCheckable(True)
#         blueb.move(10, 110)
#
#         blueb.clicked[bool].connect(self.setColor)
#
#         self.square = QFrame(self)
#         self.square.setGeometry(150, 20, 100, 100)
#         self.square.setStyleSheet("QWidget { background-color: %s }" %
#                                   self.col.name())
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('Toggle button')
#         self.show()
#
#     def setColor(self, pressed):
#
#         source = self.sender()
#
#         if pressed:
#             val = 255
#         else:
#             val = 0
#
#         if source.text() == "Red":
#             self.col.setRed(val)
#         elif source.text() == "Green":
#             self.col.setGreen(val)
#         else:
#             self.col.setBlue(val)
#
#         self.square.setStyleSheet("QFrame { background-color: %s }" %
#                                   self.col.name())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QProgressBar,
#                              QPushButton, QApplication)
# from PyQt5.QtCore import QBasicTimer
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#
#         self.btn = QPushButton('Start', self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#
#         self.timer = QBasicTimer()
#         self.step = 0
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QProgressBar')
#         self.show()
#
#     def timerEvent(self, e):
#
#         if self.step >= 100:
#             self.timer.stop()
#             self.btn.setText('Finished')
#             self.step = 0
#             return
#
#         self.step = self.step + 1
#         self.pbar.setValue(self.step)
#
#     def doAction(self):
#
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
#                              QLabel, QApplication)
# from PyQt5.QtCore import QDate
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         cal = QCalendarWidget(self)
#         cal.setGridVisible(True)
#         cal.move(20, 20)
#         cal.clicked[QDate].connect(self.showDate)
#
#         self.lbl = QLabel(self)
#         date = cal.selectedDate()
#         self.lbl.setText(date.toString())
#         self.lbl.move(130, 260)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle('Calendar')
#         self.show()
#
#     def showDate(self, date):
#         self.lbl.setText(date.toString())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
#                              QLabel, QApplication)
# from PyQt5.QtGui import QPixmap
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#         pixmap = QPixmap("123.jpg")
#
#         lbl = QLabel(self)
#         lbl.setPixmap(pixmap)
#
#         hbox.addWidget(lbl)
#         self.setLayout(hbox)
#
#         self.move(300, 200)
#         self.setWindowTitle('Big tits')
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel,
#                              QLineEdit, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.lbl = QLabel(self)
#         qle = QLineEdit(self)
#
#         qle.move(60, 100)
#         self.lbl.move(60, 40)
#
#         qle.textChanged[str].connect(self.onChanged)
#
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QLineEdit')
#         self.show()
#
#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel,
#                              QComboBox, QApplication)
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         self.lbl = QLabel("Ubuntu", self)
#
#         combo = QComboBox(self)
#         combo.addItem("Ubuntu")
#         combo.addItem("Mandriva")
#         combo.addItem("Fedora")
#         combo.addItem("Arch")
#         combo.addItem("Gentoo")
#
#         combo.move(50, 50)
#         self.lbl.move(50, 150)
#
#         combo.activated[str].connect(self.onActivated)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QComboBox')
#         self.show()
#
#     def onActivated(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame,
#                              QSplitter, QStyleFactory, QApplication)
# from PyQt5.QtCore import Qt
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#         hbox = QHBoxLayout(self)
#
#         topleft = QFrame(self)
#         topleft.setFrameShape(QFrame.StyledPanel)
#
#         topright = QFrame(self)
#         topright.setFrameShape(QFrame.StyledPanel)
#
#         bottom = QFrame(self)
#         bottom.setFrameShape(QFrame.StyledPanel)
#
#         splitter1 = QSplitter(Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)
#
#         splitter2 = QSplitter(Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#
#         hbox.addWidget(splitter2)
#         self.setLayout(hbox)
#
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QSplitter')
#         self.show()
#
#     def onChanged(self, text):
#         self.lbl.setText(text)
#         self.lbl.adjustSize()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())