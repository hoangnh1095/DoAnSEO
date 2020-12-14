
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

import laydulieu as getData

from tkcalendar import Calendar, DateEntry

#Variables
HEIGHT=200
WIDTH=600



#function
def popup_showinfo():
    showinfo("Loading", "Đang tải dữ liệu về...")

def createNewFrame():
    showinfo("Trạng thái","Thành công !!! ")
    window = tk.Tk()
    window.title("Phần mềm phân tích trang web")
    window.geometry("+700+100")
    canvas=tk.Canvas(window,height=500,width=WIDTH,bg="white")
    canvas.pack()
    getData.getBdduong(dateStartTextField.get("1.0",tk.END+"-1c"),dateEndTextField.get("1.0",tk.END+"-1c"),"unizone.edu.vn")
def getDate(num):
    def print_sel():
        if(num==1):
            dateStartTextField.configure(state='normal')
            dateStartTextField.delete("1.0","end")
            dateStartTextField.insert("1.0",cal.selection_get())
            dateStartTextField.configure(state='disable')
        else:
            dateEndTextField.configure(state='normal')
            dateEndTextField.delete("1.0","end")
            dateEndTextField.insert("1.0",cal.selection_get())
            dateEndTextField.configure(state='disable')

    top = tk.Toplevel(frame)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2020, month=9, day=1)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

   

#set up
window = tk.Tk()
window.title("Phần mềm phân tích trang web")
window.geometry("+300+100")


canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH,bg="white")
canvas.pack()

#lable frame
frame=tk.Frame(window,bg="white")
frame.place(relx=0.2,rely=0.1,relwidth=0.8,relheight=2)

lable=tk.Label(frame,text="Nhấn bắt đầu để tiến hành phân tích trang web unizone.edu.vn !!!", bg="white",font=("Times New Roman",12))

lable.grid(row=0,column=1)


dateStartTextField=tk.Text(frame,font=("Helvetica", 12),width=30,height=1)
dateStartTextField.configure(state='disable')
dateStartTextField.grid(row=2,column=1)
buttonGetDate=tk.Button(frame, text='Chọn ngày khởi đầu', command=lambda:getDate(1))
buttonGetDate.grid(row=3,column=1)
dateEndTextField=tk.Text(frame, font=("Helvetica", 12),width=30,height=1)
dateEndTextField.configure(state='disable')
dateEndTextField.grid(row=4,column=1)
buttonGetDate=tk.Button(frame, text='Chọn ngày kết thúc', command=lambda:getDate(2))
buttonGetDate.grid(row=5,column=1)
buttonGetData=tk.Button(frame,text="Bắt đầu",bg="blue",command=lambda:createNewFrame())
buttonGetData.grid(row=6,column=1)

window.mainloop()


