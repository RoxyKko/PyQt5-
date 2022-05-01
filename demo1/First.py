import sys

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #   创建QApplication类的实例
    app = QApplication(sys.argv)
    #   创建一个窗口
    w = QWidget()
    w.resize(600,450)
    #   移动窗口左上角坐标
    w.move(300,300)
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    #   显示窗口
    w.show()

    #   进入程序主循环、并通过exit函数确保主函数安全结束
    sys.exit(app.exec_())

