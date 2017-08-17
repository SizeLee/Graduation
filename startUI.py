import sys
from PyQt5.QtWidgets import QApplication

from UIPack import MainFrame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myMainWindow = MainFrame.MyMainWindow()
    sys.exit(app.exec_())