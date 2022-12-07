from pytube import YouTube
from tkinter import *
import time

#Takes text file input and divides it to array elements
Links = open("Links.txt", "r")
LinksContent = Links.read()
LinksArray  = LinksContent.split(",")

#Loops through array elements to download them
def downloadVideos():
    for n in LinksArray:
        time.sleep(1)
        YouTube(n).streams.filter(res="360p").first().download()
        num += 1


#Creates app frame
frame = Tk()

#Defines basic frame attributes
frame.title("AutoLoader")
frame.minsize(400,400)
frame.maxsize(400,400)
frame.config(bg="#FF8181")

#Label attributes
Instructions = Label(frame, text="Enter the links in the \" Links.txt \" text file\n then press download")
Instructions.place(x =70, y=10)
Instructions.config(bg="#FF8181")
Instructions.config(fg="#000000")

#Button attributes
Download = Button(frame, text="Download Videos")
Download.place(x=133, y=350)
Download.config(command=downloadVideos)



#Calls function to start the program
frame.mainloop()