from tkinter import *
from tkinter.filedialog import *
import instaloader

ig = instaloader.Instaloader()

window = Tk()
window.minsize(800, 600)



label = Label(window, text="enter username here : ")
input = Entry(window, width=30)

label.pack()
input.pack()

def download():
    username=input.get()
    ig.download_profile(username, profile_pic_only=True)
        
button = Button(window, text="télécharger l'image", command=download)
button.pack()

window.mainloop()