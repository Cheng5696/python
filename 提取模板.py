import os
from collections import  Counter
import time

# 数据类
class Data():
    def __init__(self,tpm,Chl,Barcode,TestTime,DCIR1,DCIR2,pj,V1,V2,V3,V4,I1,I2,T1,T2,T3,T4,Remark):
        self.tpm = tpm
        self.Chl = Chl
        self.Barcode = Barcode
        self.TestTime = TestTime
        self.DCIR1 = DCIR1
        self.DCIR2 = DCIR2
        self.pj = pj
        self.V1 = V1
        self.V2 = V2
        self.V3 = V3
        self.V4 = V4
        self.I1 =I1
        self.I2 =I2
        self.T1 = T1
        self.T2 =T2
        self.T3 = T3
        self.T4 = T4
        self.Remark = Remark


# 读取文件父类
class Read():
    def __init__(self,Lujing):
        self.Lujing = Lujing

    def Read(self):
        pass

 # 读取文件子类
class ReadCsv(Read):
    def Read (self):
        DataLists = []
        TPMtemp = None
        with open(self.Lujing) as csvFile:
            for line in csvFile:
                # 字符串数据处理
                line = line.strip()
                Datalist = line.split(",")

                # 创建装有Data对象的列表
                if Datalist[0] == "托盘码":
                    TPMtemp = Datalist[1]
                elif Datalist[0] != "Chl":
                    DataClass = Data(TPMtemp,Datalist[0],Datalist[1],Datalist[2],Datalist[3],Datalist[4],Datalist[5],Datalist[6],
                         Datalist[7],Datalist[8],Datalist[9],Datalist[10],Datalist[11],Datalist[12],Datalist[13],
                         Datalist[14],Datalist[15],Datalist[16])
                    DataLists.append(DataClass)
        return DataLists


# 提取文件类
class Total ():
    def __init__(self,path):
        self.path = path

    # 读取文件夹内文件名返回列表
    def ReadDir (self):
        return os.listdir(self.path)

    # 读取文件
    def ReadFile (self):
        TotoList = []
        for filepath in self.ReadDir():
            TotoList =  TotoList + ReadCsv(self.path + filepath).Read()
        return TotoList

# 输入路径处理函数
def inputPath (path):
    path = path.replace("\\","/")
    path = path + "/"
    return path

# 数据统计类
class Tq ():
    data = []
    oknum = []
    ngnum = []
    time = []
    minTime = None
    maxTime = None
    def __init__(self,path):
        self.path = inputPath (path)

    # 提取需要的列表
    def TqFile (self):
        self.data = Total(self.path).ReadFile()
        # 统计电芯个数
        print(f"总共有{len(self.data)}个电芯")

        # 统计ok
        for temp in self.data:
            if temp.pj =="OK":
                self.oknum.append(temp.Chl)
            if temp.pj =="NG":
                self.ngnum.append(temp.Chl)

        # 统计时间
        timeTemp = []
        for i in self.data:
            timeTemp.append(i.TestTime)
        for temp in timeTemp:
            self.time.append(time.strptime(temp,"%Y-%m-%d %H:%M:%S"))
        self.maxTime = time.strftime("%Y-%m-%d %H:%M:%S", max(self.time))
        self.minTime = time.strftime("%Y-%m-%d %H:%M:%S", min(self.time))

    # 打印
    def printTest (self):
        self.TqFile()
        print(f"测试时间 {self.minTime} -> {self.maxTime}")
        print(f"共NG{len(self.ngnum)}, 共OK{len(self.oknum)}  良率{len(self.oknum) / len(self.data)}")
        for i in Counter(self.ngnum).most_common():
            print(f"通道号:{i[0]} , ng次数 {i[1]}")




# 保存测试结果到文件
class FileWrite():
    def __init__(self,path,test):
        self.path = path
        self.test = test

    def Write (self):
        with open(self.path,"a") as file:
            file.write(self.test)



if __name__ == "__main__":
    print("使用说明:")
    print("1. 复制待测数据到桌面文件夹内")
    print("2. 拷贝文件夹路径")
    print("3. 粘贴路径并回车")
    print("路径:",end="")

    test = Tq(input())
    test.printTest()
    txt = "\n"+str(test.minTime)+"   ->   "+str(test.maxTime) + "\n" + "     共NG" + str(len(test.ngnum)) + "     共OK" + str(len(test.oknum)) +"     良率"+ str(len(test.oknum) / len(test.data)) +"\n" + str(Counter(test.ngnum).most_common()) + "\n"
    write = FileWrite("C:/Users/admin/Documents/TEMP/历史良率.TXT",txt)
    write.Write()
    input()


"""
**列表lists中每个元素出现的次数**  
使用函数Counter，可以迅速获取list中每个元素出现的次数
```
from collections import Counter

arr=[1,2,5,1,1,5,6,3,3,2,2,4,8]

# arr=Counter(lists)
```

**使用with来操作文件**  
```
with open("./data.txt", "r", encoding="utf-8") as file_object: 
 for line in file_object: 
 print(line.rstrip()) 
 
```
"""
