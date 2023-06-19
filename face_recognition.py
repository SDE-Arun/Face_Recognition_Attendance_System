from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

sum_has_run = False
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        self.bg = ImageTk.PhotoImage(
            file=r"images\img_img5.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        main_heading = Label(
            lbl_bg,
            text="Face Detection",
            font=("times new roman", 50, "bold", "italic"),
            fg="white",
            bg="black",
        )
        main_heading.place(x=530, y=0, width=500)

        # ================= Button to Detecting the face  ________________________
        b1_1 = Button(
            lbl_bg,
            text="Click here to 'Detect Face' ",
            cursor="hand2",
            command=self.face_recog,
            font=("times new roman", 22, "bold"),
            fg="orange",
            bg="black",
        )
        b1_1.place(x=580, y=400, width=350, height=50)

        #   ======================= Function for marking attendance -----------------------------------------

    def mark_attendance(self, i, r, n, d):
        global sum_has_run
        if sum_has_run:
            return 
        
        with open("ABC.csv", "a+", newline="\n") as f:
            # f.seek(0)
            mydataList = f.readlines()
            name_list = []
            # if len(mydataList)>0:
                # f.write("\n")
                
            for line in mydataList:
                entry = line
                name_list.append(entry[0])
            if (
                (i not in name_list)
                and (r not in name_list)
                and (n not in name_list)
                and (d not in name_list)
            ):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                sum_has_run = True


        #   ======================= Function for the face detection -----------------------------------------

    def face_recog(self):
        def draw_boundry(img, classifier, scale_factor, min_neighbour, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scale_factor, min_neighbour)
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                i_d, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(
                    user="root",
                    password="1234",
                    host="127.0.0.1",
                    database="login_table",
                    
                )
                conn._autocommit = True
                cur = conn.cursor()

                cur.execute("select Name FROM student_details where Student_id=" + str(i_d))
                n = cur.fetchall()
                n = str(n)
                # n = "+".join(n)

                cur.execute("select Roll FROM student_details where Student_id=" + str(i_d))
                r = cur.fetchone()
                r = str(r)
                # r = "+".join(r)

                cur.execute("select Dep FROM student_details where Student_id=" + str(i_d))
                d = cur.fetchone()
                d = str(d)
                # d = "+".join(d)

                cur.execute("select Student_id FROM student_details where Student_id=" + str(i_d))
                i = cur.fetchone()
                i = str(i)
                # i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img,f"Student Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img,"Unknown Face",(x, y - 5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255),3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition Phase", img)

            if cv2.waitKeyEx(1) == 13:
                break
        #  ________________________________Writing Duplicate Values issue resolves here ________________________________
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
