
from tkinter import *
from pytube import YouTube
from tkinter.filedialog import askdirectory
from tkinter import messagebox as msg
import os

root=Tk()
root.title("Youtube Video Downloader")
root.resizable(False,False)
root.geometry("450x380")
root.config(bg="black")

def select(event):
    data=askdirectory()
    try:
        dirV.set(f"{data}")
        pass
    except:
        print("you didn't selected compatible directory")
        pass
    pass
def remove(event):
    linkW.delete(0,END)
    root.update()

def download(event):
    global yt
    try:
        yt = YouTube(linkV.get())
        pass
    except:
        msg.showerror("Privacy issue","You can't download this video because of either low conection OR owner "
                                      "has restricted this video")
        print("Connection error........")
        pass
    global v
    if ext.get()==1:
        v=yt.streams.filter(type="audio").first()
        pass
    else:
        v = yt.streams.filter(type="video").first()
        pass

    try:
        msg.showinfo("Downloading started","""Your file is downloading....Please click "OK" and we will notify you when downloading is completed""")
        if dirV.get()!="Choose a folder to save file":
            v.download(dirV.get())
            pass
        else:
            v.download()
        msg.showinfo("Task completed","Successfully downloaded your file")
        pass
    except:
        print("Can't download.......")
        msg.showerror("Failed!","You can't download this video")
        pass
    pass




f=Frame(root,bg="black")
Label(f,text="URL",font="ubuntu 16 bold",bg="black",fg="white").\
    grid(row=0,column=0,sticky="NESW",padx=8,pady=7)
linkV=StringVar()
linkV.set("Enter link")
linkW=Entry(f,font="calibri 12 italic",width=30,textvariable=linkV,bg="black",fg="grey")
linkW.bind("<Button-1>",remove)
linkW.grid(row=0,column=1,sticky="NESW",pady=6)
Label(f,text="Directory",font="ubuntu 16 bold",bg="black",fg="white").\
    grid(row=1,column=0,padx=8,sticky="NESW",pady=5)
dirV=StringVar()
dirV.set("Choose a folder to save file")
dirW=Entry(f,font="calibri 12 italic",width=30,textvariable=dirV,bg="black",fg="grey")
dirW.grid(row=1,column=1,sticky="NESW",pady=6)
dirW.bind("<Button-1>",select)
Label(f,text="Mode",font="ubuntu 16 bold",bg="black",fg="white").grid(row=2,column=0,padx=8,sticky="NESW",pady=7)
ext=IntVar()
ext.set(2)
Radiobutton(f,text="Audio",value=1,variable=ext,bg="black",fg="grey",font="calibri 12 bold").\
    grid(row=2,column=1,sticky=W,pady=8)
Radiobutton(f,text="Video",value=2,variable=ext,bg="black",fg="grey",font="calibri 12 bold").\
    grid(row=2,column=1,pady=8)
downloadB=Button(f,text="Download",font="lora 13 normal",bg="black",fg="white")
downloadB.bind("<Button-1>",download)
downloadB.grid(row=3,column=1,pady=7,sticky=W)
downloadB=Button(f,text="Quit",font="lora 13 normal",bg="black",fg="white",command=quit)
downloadB.grid(row=3,column=1,pady=7,ipadx=10)
f.pack(pady=90)


root.mainloop()

