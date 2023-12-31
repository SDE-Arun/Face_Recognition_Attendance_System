from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1600x900+0+0")

        # ============= background image ================================
        self.bg = ImageTk.PhotoImage(
            file=r"images\new_img3.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        # =============================== Time in main window +++++++++++++++++++++++
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(
            lbl_bg,
            font=("times new roman", 23, "bold"),
            fg="green2",
            bg="black",
        )
        lbl.place(x=0,y=15,width=210,height=40)
        time()

        main_heading = Label(lbl_bg,
            text="Face Recognition Attendance System",
            font=("times new roman", 50, "bold", "italic"),
            fg="black",
            bg="light coral",
        )
        main_heading.place(x=220, y=0, width=1100)

        # ============ Image / button for the student ==================
        img_std = Image.open(
            r"images\student_detal1.jpg"
        )
        img_std = img_std.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgstd = ImageTk.PhotoImage(img_std)

        b1 = Button(
            lbl_bg, image=self.photoimgstd, command=self.student_details, cursor="hand2"
        )
        b1.place(x=100, y=200, width=220, height=220)

        b1_1 = Button(
            lbl_bg,
            text="Student Details",
            cursor="hand2",
            command=self.student_details,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b1_1.place(x=100, y=400, width=220, height=40)

        # ============ Image / button for the Face Detection  ==================
        img_face = Image.open(
            r"images\face.jpg"
        )
        img_face = img_face.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgface = ImageTk.PhotoImage(img_face)

        b2 = Button(
            lbl_bg, image=self.photoimgface, command=self.face_data, cursor="hand2"
        )
        b2.place(x=450, y=200, width=220, height=220)

        b2_2 = Button(
            lbl_bg,
            text="Face Detector",
            cursor="hand2",
            command=self.face_data,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b2_2.place(x=450, y=400, width=220, height=40)

        # ============ Image / button for Attendance  ==================
        img_attend = Image.open(
            r"images\attendance.jpg"
        )
        img_attend = img_attend.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgattend = ImageTk.PhotoImage(img_attend)

        b3 = Button(
            lbl_bg,
            image=self.photoimgattend,
            cursor="hand2",
            command=self.attendance_data,
        )
        b3.place(x=800, y=200, width=220, height=220)

        b3_3 = Button(
            lbl_bg,
            text="Attendance",
            cursor="hand2",
            command=self.attendance_data,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b3_3.place(x=800, y=400, width=220, height=40)

        # ============ Image / button for Help  ==================
        img_help = Image.open(
            r"images\chatbot.png"
        )
        img_help = img_help.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimghelp = ImageTk.PhotoImage(img_help)

        b4 = Button(
            lbl_bg, image=self.photoimghelp, cursor="hand2", command=self.help_data
        )
        b4.place(x=1150, y=200, width=220, height=220)

        b4_4 = Button(
            lbl_bg,
            text="Help",
            cursor="hand2",
            command=self.help_data,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b4_4.place(x=1150, y=400, width=220, height=40)

        # ============ Image / button to train the data  ==================
        img_train = Image.open(
            r"images\train_dat.jpg"
        )
        img_train = img_train.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgtrain = ImageTk.PhotoImage(img_train)

        b5 = Button(
            lbl_bg, image=self.photoimgtrain, command=self.train_data, cursor="hand2"
        )
        b5.place(x=100, y=500, width=220, height=220)

        b5_5 = Button(
            lbl_bg,
            text="Data Training",
            command=self.train_data,
            cursor="hand2",
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b5_5.place(x=100, y=700, width=220, height=40)

        # ============ Image / button for getting the student pics  ==================
        img_photo = Image.open(
            r"images\people_pics.jpg"
        )
        img_photo = img_photo.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgphoto = ImageTk.PhotoImage(img_photo)

        b6 = Button(
            lbl_bg, image=self.photoimgphoto, cursor="hand2", command=self.open_img
        )
        b6.place(x=450, y=500, width=220, height=220)

        b6_6 = Button(
            lbl_bg,
            text="Photos",
            cursor="hand2",
            command=self.open_img,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b6_6.place(x=450, y=700, width=220, height=40)

        # ============ Image / button for Developer details  ==================
        img_developer = Image.open(
            r"images\develop.jpg"
        )
        img_developer = img_developer.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgdeveloper = ImageTk.PhotoImage(img_developer)

        b7 = Button(
            lbl_bg,
            image=self.photoimgdeveloper,
            cursor="hand2",
            command=self.developer_data,
        )
        b7.place(x=800, y=500, width=220, height=220)

        b7_7 = Button(
            lbl_bg,
            text="Developer",
            cursor="hand2",
            command=self.developer_data,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b7_7.place(x=800, y=700, width=220, height=40)

        # ============ Image / button for exit  ==================
        img_exit = Image.open(
            r"images\exit.png"
        )
        img_exit = img_exit.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimgexit = ImageTk.PhotoImage(img_exit)

        b8 = Button(
            lbl_bg, image=self.photoimgexit, cursor="hand2", command=self.exit_window
        )
        b8.place(x=1150, y=500, width=220, height=220)

        b8_8 = Button(
            lbl_bg,
            text="Exit",
            cursor="hand2",
            command=self.exit_window,
            font=("times new roman", 18, "bold"),
            fg="orange",
            bg="black",
        )
        b8_8.place(x=1150, y=700, width=220, height=40)

        # _____________________________________________________  Functions Button for pictures _____________________________________________________________

    def open_img(self):
        os.startfile("Data_Images")

        # _____________________________________________________  Functions Button for student details _____________________________________________________

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

        # _____________________________________________________  Functions Button to Train Dataset  _____________________________________________________

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    # _____________________________________________________  Functions Button to face detector  _____________________________________________________
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    # _____________________________________________________  Functions Button for attendance  _____________________________________________________
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    # _____________________________________________________  Functions Button for developer Profile  _____________________________________________________
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    # _____________________________________________________  Functions Button for getting help  _____________________________________________________
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    # _____________________________________________________  Functions Button for exit from window  _____________________________________________________
    def exit_window(self):
        self.iexit = tkinter.messagebox.askyesno(
            "Face Recognition",
            "Are you sure, to exit from this Project !",
            parent=self.root,
        )
        if self.iexit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    print(root)
    obj = Face_Recognition_System(root)
    root.mainloop()
