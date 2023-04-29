"""
2023/04/29  python 3.11
用继承Theader的方法实现多线程
模拟下载两本小说
"""
from time import time,sleep
from threading import Thread
from random import randint


class Download (Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self) :
        print(f"正在下载{self.name}")
        ran_time = randint(5, 10)
        sleep(ran_time)
        print(f"下载{self.name}完毕，用时{ran_time}")


def main():
    start_time = time()
    p1 = Download("母猪的产后护理.txt")
    p2 = Download("葫芦娃.txt")
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end_time = time()
    print(f"一共用时{-start_time+end_time}秒")


if __name__ == "__main__":
    main()
