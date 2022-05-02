import sys
import demo5_1

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = demo5_1.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    #控件尺寸最大最小值、尺寸策略
    #我们得到按钮控件的期望尺寸（sizeHint）为32*23（宽*高）