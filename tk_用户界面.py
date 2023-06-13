import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
FilePath = filedialog.askopenfilename()
print(FilePath)