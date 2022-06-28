from PyQt5 import QtCore, QtGui, QtWidgets
import demo1,demo2,demo3
import sys


# def open(self):
#     import demo3, demo2
#     self.child1 = demo2.Ui_child1()
#     self.child2 = demo3.Ui_child2()
#     self.child1.show()
#     self.child2.show()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=demo1.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.setWindowFlags(QtCore.Qt.Dialog)#设置窗口样式

    ui.button=QtWidgets.QPushButton(ui.centralwidget)#设置按钮
    ui.button.setText("打开子窗口")
    ui.button.clicked.connect(ui.open)

    mainwindow.show()
    sys.exit(app.exec_())

    #多窗口的使用