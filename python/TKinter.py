#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019-07-13 17:48
# @Author: cainjiang
# @File  : TKinter.py
import tkinter as tk  # 使用Tkinter前需要先导入

window = tk.Tk()
window.title("MY Window")
window.geometry("500x500")

label = tk.Label(window, text='你好!', bg='green', font=('Arial', 12), width=30, height=2)
label.pack()
window.mainloop()
