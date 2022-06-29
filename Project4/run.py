from PyQt5 import QtCore, QtGui, QtWidgets
import sys,demo
from PyQt5.QtCore import Qt

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=demo.Ui_MainWindow()
    ui.setupUi(mainwindow)

    mainwindow.setWindowOpacity(1)#设置透明度

    icon=QtGui.QIcon()#设置图标
    icon.addPixmap(QtGui.QPixmap(r"8pin-DIP.png"),QtGui.QIcon.Normal,QtGui.QIcon.Off)
    mainwindow.setWindowIcon(icon)

    mainwindow.setWindowTitle("忘却的旋律")#设置窗口标题

    mainwindow.setStyleSheet("#MainWindow{border-image:url(1730.png)}")#设置窗口背景

    ui.label.setText("密码：")#设置文本
    ui.label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)#水平左对齐，垂直右对齐

    mainwindow.show()
    sys.exit(app.exec_())


    #复习窗口透明度、设置图标、标题、背景
    #label标签的内容设置，对齐设置 2022年6月29日15:14:38