from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1600x900+0+0")

        # ______________________ Variables for the Data feeding _________________________
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # ================== variables for the buttons -------------------------
        self.var_radio1 = StringVar()

        # ============= background image ================================
        self.bg = ImageTk.PhotoImage(
            file=r"images\img10.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        main_heading = Label(lbl_bg,
            text="Face Recognition Attendance System",
            font=("times new roman", 50, "bold", "italic"),
            fg="black",
            bg="light coral",
        )
        main_heading.place(x=220, y=0, width=1100)
        # ================================== Main Frame ============================
        main_frame = Frame(lbl_bg, bd=2)
        main_frame.place(x=35, y=100, width=1450, height=650)

        # ====== left side of label frame ==========
        Left_frame = LabelFrame(
            main_frame,
            bd=2,
            relief=RIDGE,
            text="Student Details",
            font=("times new roman", 18, "bold"),
            bg="orange",
        )
        Left_frame.place(x=10, y=10, width=700, height=625)

        # ======== Current form inside the left frame==============
        current_form = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Current Course Details",
            font=("times new roman", 18, "bold"),
            fg="blue",
        )
        current_form.place(x=10, y=4, width=680, height=145)

        # ========== Department level Combobox============
        dept_label = Label(
            current_form, text="Department", font=("times new roman", 13, "bold")
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        dept_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        dep_combo = ttk.Combobox(
            current_form,
            textvariable=self.var_dep,
            font=("times new roman", 13, "bold"),
            width=22,
            state="readonly",
        )
        dep_combo["values"] = (
            "Select Your Department",
            "Computer Science",
            "Statistics",
            "Mathematics",
            "Physics",
        )
        dep_combo.current(1)  # to fix index 0 at all the time in our box
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # ========== Course level Combobox
        cour_label = Label(
            current_form, text="Course", font=("times new roman", 13, "bold")
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        cour_label.grid(row=0, column=2, padx=20, pady=5, sticky=W)

        cour_combo = ttk.Combobox(
            current_form,
            textvariable=self.var_course,
            font=("times new roman", 13, "bold"),
            width=22,
            state="readonly",
        )
        cour_combo["values"] = ("Select Your Course", "MCA", "BCA", "MSc", "BSc")
        cour_combo.current(1)  # to fix index 0 at all the time in our box
        cour_combo.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # ========== Year level Combobox==========
        year_label = Label(
            current_form, text="Year", font=("times new roman", 13, "bold")
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        year_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        year_combo = ttk.Combobox(
            current_form,
            textvariable=self.var_year,
            font=("times new roman", 13, "bold"),
            width=22,
            state="readonly",
        )
        year_combo["values"] = ("Select Your batch", "2021-22", "2022-23", "2023-24")
        year_combo.current(1)  # to fix index 0 at all the time in our box
        year_combo.grid(row=1, column=1, padx=2, pady=20, sticky=W)

        # ========== Semester level Combobox==========
        sems_label = Label(
            current_form, text="Semester", font=("times new roman", 13, "bold")
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        sems_label.grid(row=1, column=2, padx=5, pady=15, sticky=W)

        sems_combo = ttk.Combobox(
            current_form,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_semester,
            width=22,
            state="readonly",
        )
        sems_combo["values"] = (
            "Select Your Semseter",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
        )
        sems_combo.current(0)  # to fix index 0 at all the time in our box
        sems_combo.grid(row=1, column=3, padx=2, pady=20, sticky=W)

        # ======== Class_student_information form inside the left frame==============
        class_student_form = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
            text="Class Student Information",
            font=("times new roman", 18, "bold"),
            fg="blue",
        )
        class_student_form.place(x=10, y=153, width=680, height=340)

        # ========== StudentId============
        studentId_label = Label(
            class_student_form, text="StudentId :", font=("times new roman", 13, "bold")
        )
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_std_id,
        )
        studentId_entry.grid(row=0, column=1, sticky=W)

        # ========== Student Name =================
        studentName_label = Label(
            class_student_form,
            text="Student Name :",
            font=("times new roman", 13, "bold"),
        )
        studentName_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_std_name,
        )
        studentName_entry.grid(row=1, column=1, pady=15, sticky=W)

        # ========== Class Division =================

        Class_div_label = Label(
            class_student_form,
            text="Class Division",
            font=("times new roman", 13, "bold"),
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        Class_div_label.grid(row=2, column=0, padx=5, pady=15, sticky=W)

        Class_div_combo = ttk.Combobox(
            class_student_form,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_div,
            width=17,
            state="readonly",
        )
        Class_div_combo["values"] = ("Select Your Division", "A", "B", "C", "D")
        Class_div_combo.current(1)  # to fix index 0 at all the time in our box
        Class_div_combo.grid(row=2, column=1, padx=2, pady=20, sticky=W)

        # ========== Roll No =================
        roll_no_label = Label(
            class_student_form, text="Roll no. :", font=("times new roman", 13, "bold")
        )
        roll_no_label.grid(row=3, column=0, padx=5, pady=15, sticky=W)

        roll_no_entry = ttk.Entry(
            class_student_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_roll,
        )
        roll_no_entry.grid(row=3, column=1, padx=10, pady=15, sticky=W)

        # ========== Gender =================
        gender_label = Label(
            class_student_form, text="Gender :", font=("times new roman", 13, "bold")
        )
        gender_label.grid(row=4, column=2, padx=5, pady=15, sticky=W)

        gender_combo = ttk.Combobox(
            class_student_form,
            font=("times new roman", 13, "bold"),
            width=17,
            textvariable=self.var_gender,
            state="readonly",
        )
        gender_combo["values"] = (
            "Select Your Gender",
            "Male",
            "Female",
            "Not to specify",
        )
        gender_combo.current(1)  # to fix index 0 at all the time in our box
        gender_combo.grid(row=4, column=3, pady=15, sticky=W)

        # ========== D.O.B =================
        dob_label = Label(
            class_student_form,
            text="Dob (dd/mm/yy) :",
            font=("times new roman", 13, "bold"),
        )
        dob_label.grid(row=4, column=0, padx=5, pady=15, sticky=W)

        dob_entry = ttk.Entry(
            class_student_form,
            width=20,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_dob,
        )
        dob_entry.grid(row=4, column=1, padx=10, pady=15, sticky=W)

        # ========== E-mail =================
        email_label = Label(
            class_student_form, text="e-mail :", font=("times new roman", 13, "bold")
        )
        email_label.grid(row=0, column=2, pady=15, sticky=W)

        email_entry = ttk.Entry(
            class_student_form,
            width=18,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_email,
        )
        email_entry.grid(row=0, column=3, pady=15, sticky=W)

        # ========== Phone No. =================
        phone_no_label = Label(
            class_student_form, text="Phone no. :", font=("times new roman", 13, "bold")
        )
        phone_no_label.grid(row=1, column=2, pady=15, sticky=W)

        phone_no_entry = ttk.Entry(
            class_student_form,
            width=18,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_phone,
        )
        phone_no_entry.grid(row=1, column=3, pady=15, sticky=W)

        # ========== Address =================
        address_label = Label(
            class_student_form, text="Address :", font=("times new roman", 13, "bold")
        )
        address_label.grid(row=3, column=2, pady=15, sticky=W)

        address_entry = ttk.Entry(
            class_student_form,
            width=18,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_address,
        )
        address_entry.grid(row=3, column=3, pady=15, sticky=W)

        # ========== Teacher's name =================
        teacher_name_label = Label(
            class_student_form,
            text="Teacher name :",
            font=("times new roman", 13, "bold"),
        )
        teacher_name_label.grid(row=2, column=2, pady=15, sticky=W)

        teacher_name_entry = ttk.Entry(
            class_student_form,
            width=18,
            font=("times new roman", 13, "bold"),
            textvariable=self.var_teacher,
        )
        teacher_name_entry.grid(row=2, column=3, pady=15, sticky=W)

        # _______________________ Radio Button in left side _________________________
        radio_button1 = ttk.Radiobutton(
            class_student_form,
            variable=self.var_radio1,
            text="Take Photo Sample",
            width=20,
            value="yes",
        )
        radio_button1.grid(row=5, column=0)

        radio_button2 = ttk.Radiobutton(
            class_student_form,
            text="No Photo Sample",
            width=20,
            value="No",
            variable=self.var_radio1,
        )
        radio_button2.grid(row=5, column=1)

        # _________________ Button Frame __________________________
        btn_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
        )
        btn_frame.place(x=10, y=495, width=680, height=50)

        # _________________ Button for saving the student details  __________________________
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            font=("times new roman", 13, "bold"),
            bg="sky blue",
            fg="black",
            width=15,
        )
        save_btn.grid(row=0, padx=5, column=0)

        # _________________ Button for Updating the student details  __________________________
        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            font=("times new roman", 13, "bold"),
            bg="dodger blue",
            fg="black",
            width=15,
        )
        update_btn.grid(row=0, column=1, padx=5, pady=5)

        # _________________ Button for Deleting the student details  __________________________
        delete_btn = Button(
            btn_frame,
            text="Delete",
            font=("times new roman", 13, "bold"),
            command=self.delete_data,
            bg="red",
            fg="black",
            width=15,
        )
        delete_btn.grid(row=0, column=3, padx=5, pady=5)

        # _________________ Button for Reseting the student details  __________________________
        reset_btn = Button(
            btn_frame,
            text="Reset",
            font=("times new roman", 13, "bold"),
            command=self.reset_data,
            bg="cyan",
            fg="black",
            width=15,
        )
        reset_btn.grid(row=0, column=2, padx=5, pady=5)

        # _________________ Pic button Frame __________________________
        pic_btn_frame = LabelFrame(
            Left_frame,
            bd=2,
            relief=RIDGE,
        )
        pic_btn_frame.place(x=10, y=545, width=680, height=40)

        # ______$$$$$$$$$$$$$$$$___________ Button for taking the pic  _____________$$$$$$$$$$$$$$$$_____________
        take_pic_btn = Button(
            pic_btn_frame,
            text="Take Photo Sample",
            font=("times new roman", 13, "bold"),
            command=self.generate_dataset,
            bg="lawn green",
            fg="black",
            width=25,
        )
        take_pic_btn.grid(row=0, padx=7, pady=3, column=0)

        # ______$$$$$$$$$$$$$$$$___________ Button for updating the pic  _____________$$$$$$$$$$$$$$$$_____________
        reset_pic_btn = Button(
            pic_btn_frame,
            text="Update Photo Sample",
            font=("times new roman", 13, "bold"),
            bg="yellow",
            fg="black",
            width=25,
        )
        reset_pic_btn.grid(row=0, padx=7, pady=3, column=1)

        # _____________$$$$$$$$$$$_________________====== right side of label frame ==========_____________$$$$$$$$$$$________________$$$%%%%%%%%%%%%%%%%
        Right_frame = LabelFrame(
            main_frame,
            text="Search Window",
            font=("times new roman", 18, "bold"),
            bd=2,
            relief=RIDGE,
            bg="orange",
        )
        Right_frame.place(x=730, y=10, width=700, height=625)

        # _______________________________ Search System ____________________________________
        search_frame = Frame(
            Right_frame,
            bd=2,
            relief=RIDGE,
        )
        search_frame.place(x=10, y=7, width=680, height=140)

        # ___________ Search By column on RHS ___________

        search_label = Label(
            search_frame,
            text="Search here using: ",
            font=("times new roman", 13, "bold"),
        )
        # We are taking the help of grid format , so we can arrange our labels easily as we have flex in CSS
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(
            search_frame,
            font=("times new roman", 13, "bold"),
            width=20,
            state="readonly",
        )
        search_combo["values"] = (
            "Select Your Choice",
            "Roll_No",
            "Phone_No",
            "D.O.B",
        )
        search_combo.current(0)  # to fix index 0 at all the time in our box
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # _============== for entering the data in search bar _____________________
        search_label = Label(
            search_frame,
            text="Enter your Choice: ",
            font=("times new roman", 13, "bold"),
        )
        search_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=18, font=("times new roman", 13, "bold")
        )
        search_entry.grid(row=1, column=1, pady=15, sticky=W)

        # ___________ Button for Searching  _____________
        search_btn = Button(
            search_frame,
            text="Search",
            font=("times new roman", 13, "bold"),
            bg="sky blue",
            fg="black",
            width=12,
        )
        search_btn.grid(row=1, padx=30, pady=3, column=2)

        # ___________ Button for Show All  _____________
        show_all_btn = Button(
            search_frame,
            text="Show All",
            font=("times new roman", 13, "bold"),
            bg="sky blue",
            fg="black",
            width=10,
        )
        show_all_btn.grid(row=1, pady=3, column=3)

        # _______________________________ Search System ____________________________________
        table_frame = Frame(
            Right_frame,
            bd=2,
            relief=RIDGE,
        )
        table_frame.place(x=10, y=155, width=680, height=400)

        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dept",
                "course",
                "year",
                "sems",
                "id",
                "name",
                "div",
                "roll",
                "gender",
                "dOB",
                "email",
                "phone",
                "address",
                "teacher",
                "photo",
            ),
            xscrollcommand=Scroll_x.set,
            yscrollcommand=Scroll_y.set,
        )

        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sems", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_no")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dOB", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        # -------------------- setting the width of the column in the search window_________________________
        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sems", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dOB", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # _______________ method for adding the data **********************************___________________________________

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="login_table",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student_details VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details are Saved Successfully ",
                    parent=self.root,
                )

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

        # _______________ method for fetching the data from database **********************************___________________________________

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="login_table",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_details")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # _______________ method for fetching the data **********************************___________________________________

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # _______________ method for updating the data **********************************___________________________________

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you really want to update these details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="login_table",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "UPDATE student_details SET Dep=%s, Course=%s, Year=%s, Semester=%s, Student_id=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success",
                    "Student details are updated successfully",
                    parent=self.root,
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # _______________ method for Deleting the data **********************************___________________________________

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id must be required", parent=self.root
            )

        else:
            try:
                delete = messagebox.askyesno(
                    "Delete",
                    "Do you really want to delete these details",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="login_table",
                    )
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student_details WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Data deleted Successfully ! ", parent=self.root
                )

            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)
                
                
                
    # _______________ method for Reset the data **********************************___________________________________

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
        
        
        
    # **********************************_ Generating Dataset or Taking the photo sample  **********************************_

    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="1234",
                        database="login_table",
                    )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student_details")
                my_result=my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute(
                        "UPDATE student_details SET Dep=%s, Course=%s, Year=%s, Semester=%s, Student_id=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()==id+1,
                        ),
                    )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                
                # ******************** Loading the predefined data on face frontals from OpenCV  ********************
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                            
                            
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # By default Sacling factor = 1.3
                    # By default Minimum Neighbour = 5
                    
                    # Loop for creating the rectangle ___________________________
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                    
                # __________________________  Opening the camera for face reading _______________________________
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        # ------------- converting the image to gray scale ______________________
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        # ___________ storing the images as name specified ======================
                        file_name_path="Data_Images/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                
                    # ___________________________ when our system stop taking samples ___________
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                        
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set Completed !!!")
                
                
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)  
           
                

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
