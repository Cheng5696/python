import tkinter as tk
from tkinter import filedialog

'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()
FolderPath=filedialog.askdirectory() #如果有特殊需要，非要选择文件夹，这个可以去掉注释使用
FilePath=filedialog.askopenfilename() #一般这个直接选择文件，会比较符合人们的使用习惯和软件的用户体验

print(FilePath)
print(FolderPath)

# C:/Users/##/Desktop/结果.json
# C:/Users/##/Desktop
