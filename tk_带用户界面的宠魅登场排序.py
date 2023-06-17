import tkinter as tk
from tkinter import filedialog
import jieba
from pyecharts.charts import Bar

window = tk.Tk()


window.title("小说出现词频排序")
window.geometry("500x500")

FilePath = ""
FolderPath = ""
data = "默认"
x = []
y = []

def getFile():
    global FilePath
    global lis
    global data
    global x
    global y
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


def table():
    for i in data[1:10]:
        x.append(i[0])
        y.append(i[1])
    bar = Bar()
    bar.add_xaxis(x)
    bar.add_yaxis("词汇",y)
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    # 也可以传入路径参数，如 bar.render("mycharts.html")
    bar.render(FolderPath+"/"+FilePath.split("/")[-1]+".html")

def saveFile():
    global data
    global FolderPath
    FolderPath = filedialog.askdirectory()

    with open(FolderPath+"/"+FilePath.split("/")[-1],"w") as f:
        f.write(str(data))

t = tk.Text(window,height=30)
t.pack()

b = tk.Button(window,
              text="打开文件",
              width=15,height=1,
              command=getFile)
b.pack()

# 保存数据按钮
b2 = tk.Button(window,
               text="保存数据",
               width=15,height=1,
               command=saveFile)
b2.pack()

# 导出表格按钮
b3 = tk.Button(window,
               text="导出表格",
               width=15,height=1,
               command=table)
b3.pack()

window.mainloop()

table()