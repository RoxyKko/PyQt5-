import sys
import project1

from PyQt5 import QtCore, QtGui, QtWidgets

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=project1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())