from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        self.bg = ImageTk.PhotoImage(
            file=r"images\img6.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        main_heading = Label(lbl_bg,
            text="Train Dataset",
            font=("times new roman", 50, "bold", "italic"),
            fg="red",
            # bg="pink",
        )
        main_heading.place(x=480, y=0, width=500)

        # ================= Button to Train Data ________________________
        b1_1 = Button(
            lbl_bg,
            text="Click here to 'Train Data' ",
            cursor="hand2",
            command=self.train_classifier,
            font=("times new roman", 22, "bold"),
            fg="orange",
            bg="black",
        )
        b1_1.place(x=580, y=480, width=350, height=50)


#   ======================= Function to train the data  -----------------------------------------
    def train_classifier(self):
        data_dir = "Data_Images"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")  # for gray scale image
            imageNP = np.array(img, "uint8")
            i_d = int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNP)
            ids.append(i_d)
            cv2.imshow("Training", imageNP)
            cv2.waitKeyEx(1)==13

        ids = np.array(ids)

        # ========================== Train the classifier and saving the data ========================
        clf = cv2.face.LBPHFaceRecognizer.create() 
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training of dataset is Completed Successfully !",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
