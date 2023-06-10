import tkinter as tk
from tkinter import filedialog
import jieba

window = tk.Tk()


window.title("小说出现词频排序")
window.geometry("500x500")

FilePath = ""
data = "默认"

def getFile():
    global FilePath
    global lis
    global data
    t.delete("1.0", "end")
    FilePath = filedialog.askopenfilename()
    with open(FilePath, "r", encoding="utf-8") as f:
        li = jieba.lcut(f.read())
        count = {}
        for i in li:
            if len(i) == 1:
                continue
            else:
                count[i] = count.get(i, 0) + 1
        li1 = list(count.items())
        li1.sort(key=lambda x: x[1], reverse=False)
        li1  = li1[::-1]
        data = li1[1:100]
        t.insert("end",str(data))  # 设置标签内容


def saveFile():
    global data
    FolderPath = filedialog.askdirectory()

    with open(FolderPath+"/"+FilePath.split("/")[-1],"w") as f:
        f.write(str(data))

t = tk.Text(window,height=30)
t.pack()

b = tk.Button(window,
              text="打开文件",
              width=15,height=2,
              command=getFile)
b.pack()


# 保存数据按钮
b2 = tk.Button(window,
               text="保存数据",
               width=15,height=20,
               command=saveFile)
b2.pack()

window.mainloop()

