from tkinter import *
from PIL import Image,ImageTk
deba_root= Tk()

deba_root.geometry("555x555")
#photo = PhotoImage(file="C:\\Users\\Debashish\\Desktop\\Face Recognisation system\\college images\\3.JPEG")

image=Image.open("C:\\Users\\Debashish\\Desktop\\Face Recognisation system\\college images\\3.JPEG")
photo=ImageTk.PhotoImage(image)
deba_label= Label(image=photo)
deba_label.pack()
deba_root.mainloop()