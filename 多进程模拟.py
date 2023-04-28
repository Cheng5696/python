"""
一个多进程模拟程序
"""
from multiprocessing import Process
from  os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print(f"进程号是:[{getpid()}]")
    print(f"开始下载{filename}")
    time_download = randint(5,10)
    sleep(time_download)
    print(f"下载{filename}完成，用了{time_download}秒")

def main ():
    stat_time = time()
    p1 =  Process(target=download_task,args=("重启末日.txt",))   # 如果不加,就会默认一个字符一个参数
    p1.start()
    p2 = Process(target=download_task,args=("重生之我是事业家.txt",))
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print(f"一共花费{end_time-stat_time}")
if __name__ == "__main__":
    main()