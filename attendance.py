from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv 
from tkinter import filedialog

mydata=list()
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1600x900+0+0")
        
    # ______________________ Variables for the Data feeding _________________________
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        

        self.bg = ImageTk.PhotoImage(
            file=r"images\fourth.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        main_heading = Label(
            lbl_bg,
            text="Attendance Database",
            font=("times new roman", 50, "bold", "italic"),
            fg="black",
            bg="tomato2",
        )
        main_heading.place(x=390, y=0, width=800)
        # ================================== Main Frame ============================
        main_frame = Frame(lbl_bg, bd=2)
        main_frame.place(x=35, y=100, width=1450, height=650)

        # =========================== left side of label frame ==========
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            font=("times new roman", 18, "bold"),
            bg="orange",
        )
        Left_frame.place(x=10, y=10, width=700, height=625)

        img_left = Image.open(r"images\att.jpg")
        img_left = img_left.resize((700, 300), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=700, height=300)

        # ========================= Current form inside the left frame==============
        current_form = Frame(
            Left_frame,
            bd=2,
            bg="wheat",
        )
        current_form.place(x=10, y=310, width=680, height=250)

        # +++++++++++++++++++++++++++++++++++ Labels and Enteries Inside the Left Frame -> Current Frame +++++++++++++++++++++++++++++++++++
        
        # ========== Attendance ID   +++++++++++++++ =================
        attendanceId_label = Label(
            current_form, text="AttendanceId :", font=("times new roman", 13, "bold")
        )
        attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_id,
        )
        attendanceId_entry.grid(row=0, column=1, sticky=W)

        # ========== Student Name ++++++++++++++++++=================
        studentName_label = Label(
            current_form,
            text="Name :",
            font=("times new roman", 13, "bold"),
        )
        studentName_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        studentName_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_name,
        )
        studentName_entry.grid(row=1, column=1, pady=15, sticky=W)

        # ========== Date +++++++++++++++++++++++++++=================
        
        date_label = Label(
            current_form,
            text="Date :",
            font=("times new roman", 13, "bold"),
        )
        date_label.grid(row=2, column=0, padx=5, pady=15, sticky=W)

        date_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_date,
        )
        date_entry.grid(row=2, column=1, pady=15, sticky=W)


        # ========== Department =++++++++++++++++++++++================
        department_label = Label(
            current_form, text="Department :", font=("times new roman", 13, "bold")
        )
        department_label.grid(row=3, column=0, padx=5, pady=15, sticky=W)

        department_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_dep,
        )
        department_entry.grid(row=3, column=1, padx=10, pady=15, sticky=W)
        
        # ========== Roll ======+++++++++++++++++++++++++===========
        roll_label = Label(
            current_form, text="Roll No. :", font=("times new roman", 13, "bold")
        )
        roll_label.grid(row=1, column=2, padx=5, pady=15, sticky=W)

        roll_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_roll,
        )
        roll_entry.grid(row=1, column=3, padx=10, pady=15, sticky=W)
        
        # ========== Time ======+++++++++++++++++++++++++===========
        time_label = Label(
            current_form, text="Time :", font=("times new roman", 13, "bold")
        )
        time_label.grid(row=2, column=2, padx=5, pady=15, sticky=W)

        time_entry = ttk.Entry(
            current_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_time,
        )
        time_entry.grid(row=2, column=3, padx=10, pady=15, sticky=W)
        
        # ========== Attendance options  ======+++++++++++++++++++++++++===========
        
        attendance_label = Label(
            current_form,
            text="Class Division",
            font=("times new roman", 13, "bold"),
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        attendance_label.grid(row=0, column=2, padx=5, pady=15, sticky=W)

        attendance_combo = ttk.Combobox(
            current_form,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_atten_attendance,
            width=17,
            state="readonly",
        )
        attendance_combo["values"] = ("Status", "Present", "Absent")
        attendance_combo.current(0)  # to fix index 0 at all the time in our box
        attendance_combo.grid(row=0, column=3, padx=2, pady=20, sticky=W)
        
        
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
         # _________________ Button Frame __________________________
        btn_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
        )
        btn_frame.place(x=10, y=560, width=680, height=50)

        # _________________ Button for importing the CSV File __________________________
        import_btn = Button(
            btn_frame,
            text="Import csv",
            command=self.import_csv,
            font=("times new roman", 13, "bold"),
            bg="sky blue",
            fg="black",
            width=20,
        )
        import_btn.grid(row=0, padx=5, column=0)

        # _________________ Button for exporting the CSV File __________________________
        export_btn = Button(
            btn_frame,
            text="Export csv",
            command=self.export_csv,
            font=("times new roman", 13, "bold"),
            bg="dodger blue",
            fg="black",
            width=20,
        )
        export_btn.grid(row=0, column=1, padx=7, pady=5)

        # # _________________ Button for Updating the attendance details  __________________________
        # update_btn = Button(
        #     btn_frame,
        #     text="Update",
        #     font=("times new roman", 13, "bold"),
        #     # command=self.delete_data,
        #     bg="tomato",
        #     fg="black",
        #     width=15,
        # )
        # update_btn.grid(row=0, column=3, padx=5, pady=5)

        # _________________ Button for Reseting the attendance details  __________________________
        reset_btn = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 13, "bold"),
            command=self.reset_cursor,
            bg="cyan",
            fg="black",
            width=20,
        )
        reset_btn.grid(row=0, column=2, padx=7, pady=5)

        # =========================== Right side of label frame ===========================================
        Right_frame = LabelFrame(
            main_frame,
            text="Student Details",
            font=("times new roman", 18, "bold"),
            bd=2,
            relief=RIDGE,
            bg="orange",
        )
        Right_frame.place(x=730, y=10, width=700, height=625)
        
        # _______________________________ Search System ____________________________________
        table_frame = Frame(
            Right_frame,
            bd=2,
            relief=RIDGE,
        )
        table_frame.place(x=10, y=7, width=680, height=580)
        
        
        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        
        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "id",
                "roll",
                "name",
                "department",
                "time",
                "date",
                "attendance",
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Attendance Id")
        self.student_table.heading("roll", text="Roll_no")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("attendance", text="Attendance")
        self.student_table["show"] = "headings"
        
        # -------------------- setting the width of the column in the search window_________________________
        self.student_table.column("id", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("department", width=100)
        self.student_table.column("time", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("attendance", width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
         # _________________ function to import the  data  __________________________
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)
            
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
                
            self.fetch_data(mydata)
        
        
             # _________________ function to export the  data  __________________________
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
        
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" Successfully")
                
        except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
                
                
        # _________________ function to reflect the data in columns__________________________
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
        
                # _________________ function to reset the data __________________________
    def reset_cursor(self):

        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

        


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
