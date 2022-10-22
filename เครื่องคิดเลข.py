from logging import root
from tkinter import *
from tkinter import font

root = Tk()
root.title("เครื่องคิดเลข")
root.mathloop()

#เเสดงผล (5*4)
display = Entry(font=('arial',30,'bold'),fg="white",bg="black")

#รับค่าปุ่ม