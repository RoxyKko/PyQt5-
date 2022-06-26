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
    ui=project1.Ui_MainWindow()


    icon = QtGui.QIcon()  # 改变图标
    # icon.addPixmap(QtGui.QPixmap(r"D:\allProject\PyQt5_Project\Project1\7F263D99B929E0B4D25F25B314F1EC0F.jpg"),QtGui.QIcon.Normal,QtGui.QIcon.Off)     #使用了绝对路径
    icon.addPixmap(QtGui.QPixmap(r"7F263D99B929E0B4D25F25B314F1EC0F.jpg"),QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 放在同级目录可以这样简写
    mainwindow.setWindowIcon(icon)
    # mainwindow.setStyleSheet("#Test{background-color:blue}")        #指定为背景图片，#Test：#号后跟想要设置的窗口ObjectName即窗口对象名称
    # mainwindow.setStyleSheet("#Test{border-image:url(borderImage.jpg)}")        #使用绝对路径要用斜杠而不是反斜杠（D:/allProject/PyQt5_Project/Project1/borderImage.jpg）

    # 另一种办法设置窗口背景图片、颜色
    palette = QtGui.QPalette()
    # palette.setColor(QtGui.QPalette.Background , Qt.red)
    # palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("./borderImage.jpg")))        #这样有时候会只显示图片的一部分
    palette.setBrush(QtGui.QPalette.Background, QBrush(
        QPixmap("./borderImage.jpg").scaled(mainwindow.size(), QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation)))  # 图片缩放显示

    mainwindow.setPalette(palette)
    mainwindow.setPalette(palette)
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())

    #改变窗口标题 2022年6月26日20:57:51
    #改变窗口大小 2022年6月26日20:58:02
    #获取屏幕大小 2022年6月26日21:06:21
    #改变窗口图标 2022年6月26日21:17:38
    #改变窗口背景颜色 2022年6月26日21:41:10
    #改变窗口背景图片 2022年6月26日21:41:27