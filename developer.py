from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1600x900+0+0")
        
        # ============= background image ================================
        self.bg = ImageTk.PhotoImage(file=r"images\img1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)
        
        f_lbl = Label(lbl_bg,text="Hello Guys, My name is Arun Chaudhary",font=("times new roman", 50, "bold","italic"),
            fg="black",
            bg="white",)
        f_lbl.place(x=140, y=0, width=1300)
        
        m_lbl = Label(lbl_bg,text="for further Information ** ",font=("times new roman", 30, "bold","italic"),
            fg="black",
            bg="white",)
        m_lbl.place(x=140, y=670, width=1300)
        l_lbl = Label(lbl_bg,text="e-mail me at:- arunkhw1998@gmail.com",font=("times new roman", 30, "bold","italic"),
            fg="black",
            bg="white",)
        l_lbl.place(x=140, y=720, width=1300)
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
