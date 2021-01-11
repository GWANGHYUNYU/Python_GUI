from tkinter import *

root = Tk()
root.title("Gwanghyun GUI")

root.geometry("640x480")    # 가로 * 세로

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

btn1 = Button(root, text="클릭",  command=change)
btn1.pack()

root.mainloop()