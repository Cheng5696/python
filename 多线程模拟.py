from random import randint
from threading import   Thread
from time import time ,sleep
def download(filename):
    print(f"开始下载{filename}")
    time_download = randint(5,10)
    sleep(time_download)
    print(f"下载{filename}用时{time_download}")

def main():
    stat_time = time()
    t1 = Thread(target=download,args=("我的奋斗.txt",))
    t1.start()
    t2 = Thread(target=download,args=("我的人生.txt",))
    t2.start()
    t1.join()
    t2.join()
    end_time = time()
    print(f"总共花费{end_time-stat_time}")

if __name__ == "__main__":
    main()