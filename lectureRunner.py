from tkinter import *
import os,sys


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("CMPUT 275 Lecture Runner")

        self.label = Label(master, text = "Choose the lecture:")
        self.label.pack()

        self.listbox = Listbox(master)
        self.listbox.pack()
        for file in os.listdir("./LECTURES"):
            if file.endswith(".ipynb"):
                self.listbox.insert(END, os.path.join("", file))

        self.close_button = Button(master, text= "Open", command=self.openLecture)
        self.close_button.pack()

        self.cls = Button(master, text="Close", command=self.close)
        self.cls.pack()
    def openLecture(self):
        os.system("ipython notebook " + self.listbox.get(ACTIVE))
    def close(self):
        self.master.quit()
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
