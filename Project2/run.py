from PyQt5 import QtCore, QtGui, QtWidgets
import Project2
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=Project2.Ui_MainWindow()
    ui.setupUi(mainwindow)

    icon = QtGui.QIcon()  # 改变图标
    icon.addPixmap(QtGui.QPixmap(r"3_1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    mainwindow.setWindowIcon(icon)

    mainwindow.setStyleSheet("#MainWindow{border-image:url(2.jpg)}")

    mainwindow.show()
    sys.exit(app.exec_())

    #设置窗口透明度2022年6月28日13:32:39
    #复习控制窗口大小、设置窗口图标、背景2022年6月28日13:41:22