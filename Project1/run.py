import sys
import project1

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget          #导入屏幕类
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush,QPixmap
import project1

if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    mainwindow=QtWidgets.QMainWindow()
    ui=project1.Ui_test()

    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

    #改变窗口标题 2022年6月26日20:57:51
    #改变窗口大小 2022年6月26日20:58:02
    #获取屏幕大小 2022年6月26日21:06:21
    #改变窗口图标 2022年6月26日21:17:38
    #改变窗口背景颜色 2022年6月26日21:41:10
    #改变窗口背景图片 2022年6月26日21:41:27