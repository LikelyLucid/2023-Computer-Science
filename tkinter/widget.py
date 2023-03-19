from tkinter import *
root = Tk()

root.maxsize(800, 200)
root.title("main window")

root.geometry("600x200")
greeting = Label(root, text="Hello")

greeting.pack()
root.mainloop()
