from PyQt5 import QtCore, QtGui, QtWidgets
import sys,demo
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
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

    ui.label.setGeometry(QtCore.QRect(150,150,300,200))#设置label的位置和大小
    # ui.label.setText("密码：1145141919810")#设置文本

    ui.label.setText("<a href='www.bilibili.com'>哔哩哔哩</a>")#设置超链接
    ui.label.setOpenExternalLinks(True)#允许打开超链接

    ui.label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)#水平左对齐，垂直右对齐
    ui.label.setWordWrap(True)#换行显示

    # ui.label.setPixmap(QPixmap("48319254.jpg"))#设置label显示图片

    print(ui.label.text())

    mainwindow.show()
    sys.exit(app.exec_())


    #复习窗口透明度、设置图标、标题、背景
    #label标签的内容设置，对齐设置 2022年6月29日15:14:38
    #label标签位置大小、换行设置   2022年6月29日15:38:04
    #设置label标签超链接           2022年6月29日15:41:52
    #设置label标签显示图片          2022年6月29日15:46:10
    #获取label标签文本                2022年6月29日15:47:17
