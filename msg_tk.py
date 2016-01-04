# ch17_03.py
# common dialogs

import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.colorchooser import *


# messagebox
print('demo messagebox')
messagebox.showinfo('Information', 'This is message')
messagebox.showerror('Error', 'This is error message')
messagebox.showwarning('Warning', 'This is warning message')

# filedialog
dir = filedialog.askdirectory()
print('selected directory:', dir)
file = filedialog.askopenfile(mode="r")
print('selected file:', file.name)
new_file_name = filedialog.asksaveasfilename()
print('save as file:', new_file_name)


# colorchooser
def get_color():
    color = askcolor()
    print('selected color:', color)

dialog = tk.Tk()
tk.Button(dialog, text='Select Color', command=get_color).pack()
dialog.title('Simple Form')
dialog.mainloop()


