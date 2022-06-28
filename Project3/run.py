from PyQt5 import QtCore, QtGui, QtWidgets
import demo1,demo2,demo3
import sys
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=demo1.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.setWindowFlags(QtCore.Qt.Dialog)#设置窗口样式

    ui.button=QtWidgets.QPushButton(ui.centralwidget)#设置按钮
    ui.button.setText("打开子窗口")

    mainwindow.show()
    sys.exit(app.exec_())