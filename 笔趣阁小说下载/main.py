from PyQt5.QtCore import  QThread, pyqtSignal
from ui import Ui_MainWindow  # 导入 uiDemo4.py 中的 Ui_MainWindow 界面类
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys
from p import novel

"""子线程类，用于执行耗时任务"""
class WorkerThread(QThread):
    # 定义一个信号，用于通知任务完成
    finished = pyqtSignal()

    def __init__(self,url,root):
        super().__init__()
        self.url = url
        self.root = root

    # 用于执行耗时任务
    def run(self):
        print("开始执行耗时任务")
        n = novel(self.url,
                  self.root,
                  r"第.{0,6}章.{0,20}")
        n.start()
        print("执行完成")
        self.finished.emit()  # 任务完成后发送信号


class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        self.root = ""

    def selectUrl (self):
        folderPath = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folderPath:
            self.label.setText(folderPath)
            self.root = folderPath
            print(folderPath)

    """槽任务"""
    def start (self):
        url = self.lineEdit.text()
        self.progressBar.setRange(0, 0)

        # 创建并启动子线程
        self.worker_thread = WorkerThread(url,self.root)
        self.worker_thread.finished.connect(self.task_finished)  # 连接任务完成信号
        self.worker_thread.start()

    def task_finished(self):
        # 任务完成后停止进度条
        self.progressBar.setRange(0, 1)
        self.progressBar.setValue(1)
        print("任务完成")




if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序