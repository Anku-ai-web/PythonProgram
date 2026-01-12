import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

root=tk.Tk()
root.title('Digital Clock')

root.geometry('400x200')
root.config(bg='black')

label = tk.Label(root, font=('calibri', 40,'bold'), background='black', foreground='white')

label.pack(anchor='center')

time()
root.mainloop()