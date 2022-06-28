from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import Project2
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=Project2.Ui_MainWindow()
    ui.setupUi(mainwindow)

    mainwindow.setWindowOpacity(1)#设置窗口透明度

    icon = QtGui.QIcon()  # 改变图标
    icon.addPixmap(QtGui.QPixmap(r"3_1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    mainwindow.setWindowIcon(icon)

    mainwindow.setStyleSheet("#MainWindow{border-image:url(2.jpg)}")#设置背景

    mainwindow.setWindowFlags(Qt.WindowCloseButtonHint)#设置窗口样式,只显示关闭按键

    mainwindow.show()
    sys.exit(app.exec_())

    #设置窗口透明度2022年6月28日13:32:39
    #复习控制窗口大小、设置窗口图标、背景2022年6月28日13:41:22
    #学会了把生成程序与启动程序分开，以后重新生成不会覆盖设置了，需要把需要的更改放在setupUI函数后面，这样写的代码才会生效 2022年6月28日13:48:19
    #设置窗口样式 2022年6月28日13:57:42
    #学习使用信号与槽，连接内置的槽函数 2022年6月28日14:10:08