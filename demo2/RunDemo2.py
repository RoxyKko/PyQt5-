import sys
import  demo2

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':        # 只有在直接运行此脚本的时候才会继续往下执行
    app = QApplication(sys.argv)    #   标准写法,创建对象表示我们的应用程序
    mainWindow = QMainWindow()      #   创建窗口
    ui = demo2.Ui_MainWindow()      #   引用生成的demo3.py创建实例
    ui.setupUi(mainWindow)          #   在指定窗口里创建指定控件
    mainWindow.show()               #显示窗口
    sys.exit(app.exec_())           #进入循环
#表单布局