import tkinter as tk

window = tk.Tk()
window.title('my window')
##窗口尺寸
window.geometry('200x200')
#创建一个lable
var= tk.StringVar()    #创建变量
l =tk.Label(window,bg='yellow',width=20,height=2,text='empty')
l.pack()
#实现将选择的选项显示在lable
def print_selection():
    l.config(text='you have selected'+var.get())

#创建几个Radiobutton
r1 = tk.Radiobutton(window, text='Option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='Option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='Option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()

##显示出来
window.mainloop()
