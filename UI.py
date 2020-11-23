import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#Variables
HEIGHT=500
WIDTH=600

#function
def popup_showinfo():
    showinfo("Loading", "Đang tải dữ liệu về...")

#set up
window = tk.Tk()
window.title("Phần mềm phân tích trang web")
window.geometry("+300+100")


canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH,bg="white")
canvas.pack()

#lable frame
frame=tk.Frame(window,bg="white")
frame.place(relx=0.2,rely=0.05,relwidth=0.8,relheight=0.1)

lable=tk.Label(frame,text="Nhấn bắt đầu để tiến hành phân tích trang web unizone.edu.vn !!!", bg="white",font=("Times New Roman",12))

lable.grid(row=0,column=1)

button=tk.Button(frame,text="Bắt đầu",bg="blue",command=popup_showinfo)
button.grid(row=1,column=1)

#content frame

frame2=tk.Frame(window,bg="#99FFFF")
frame2.place(relx=0.1,rely=0.2,relwidth=0.82,relheight=0.7)

window.mainloop()


