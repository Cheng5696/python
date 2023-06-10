import jieba
import tkinter as tk
from tkinter import filedialog
import json

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
# FolderPath=filedialog.askdirectory() #如果有特殊需要，非要选择文件夹，这个可以去掉注释使用
FilePath=filedialog.askopenfilename() #一般这个直接选择文件，会比较符合人们的使用习惯和软件的用户体验



with open(path,"r",encoding="utf-8") as f:
    li = jieba.lcut(f.read())
    count = {}
    for i in li:
        if len(i) == 1:
            continue
        else:
            count[i] = count.get(i,0) + 1
    li1 = list(count.items())
    li1.sort(key=lambda x:x[1],reverse=False)


    FolderPath = filedialog.askdirectory()
    with open(FolderPath+"/结果.json","w") as f:
        f.write(json.dumps(count, indent=2,ensure_ascii=False))
        print(li1)