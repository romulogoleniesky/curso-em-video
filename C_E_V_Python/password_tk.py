#PASSWORD COM TKINTER:
from tkinter import *

janela = Tk()
janela.title('LOGIN ACCESS')
janela.iconbitmap("lock.ico")
janela ['bg']='#62FEAE'
janela.geometry('400x400')

password_label = Label(text="PASSWORD",bg="#065FD4")
password_label.place(x=100,y=100)
password = StringVar()



janela.mainloop()
