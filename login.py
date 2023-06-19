from platform import freedesktop_os_release
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")
        self.bg = ImageTk.PhotoImage(file=r"images\img8.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)
        # lbl.pack()
        
        main_heading = Label(
            text="Face Recognition Attendance System",
            font=("times new roman", 50, "bold","italic"),
            fg="black",
            bg="orange",
        )
        main_heading.place(x=220, y=0,width=1100)
        frame = Frame(self.root, bg="black")
        frame.place(x=575, y=175, width=370, height=500)

        img1 = Image.open(
            r"images\logi_img.jpg"
        )
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbling1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lbling1.place(x=705, y=174, width=105, height=100)

        get_str = Label(
            frame,
            text="Let's Start",
            font=("times new roman", 25, "bold"),
            fg="red",
            bg="black",
        )
        get_str.place(x=105, y=100)

        # ==================Labels ===================
        username = lbl = Label(
            frame,
            text="Username (or email)",
            font=("times new roman", 15, "bold"),
            fg="red",
            bg="black",
        )
        username.place(x=35, y=170)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15))
        self.txtuser.place(x=40, y=200, width=285)

        password = lbl = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            fg="red",
            bg="black",
        )
        password.place(x=35, y=250)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txtpass.place(x=40, y=280, width=285)

        # =================== Login Button ============
        loginbtn = Button(
            frame,
            command=self.login,
            text="Login",
            font=("times new roman", 15, "bold"),
            bd=3,
            relief=RIDGE,
            fg="black",
            bg="yellow",
            activeforeground="white",
            activebackground="red",
        )
        loginbtn.place(x=125, y=350, width=120, height=35)

        # =================== Register Button ============
        registerbtn = Button(
            frame,
            text="New User Register",
            font=("times new roman", 12, "bold"),
            command=self.register_window,  # adding our new window with the register window
            borderwidth=0,
            fg="fuchsia",
            bg="black",
            activeforeground="white",
            activebackground="red",
        )
        registerbtn.place(x=17, y=410, width=160)

        # =================== Forget password Button ============
        # forgetbtn = Button(
        #     frame,
        #     text="Forget Password",
        #     command=self.forgot_password_window,
        #     font=("times new roman", 12, "bold"),
        #     borderwidth=0,
        #     fg="fuchsia",
        #     bg="black",
        #     activeforeground="white",
        #     activebackground="red",
        # )
        # forgetbtn.place(x=10, y=445, width=160)

    # =========== adding register page with the link given in login page=============================
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ========== method for the login button =================
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "all fields are required")
        elif self.txtuser.get() == "arun" and self.txtpass.get() == "1234":
            messagebox.showinfo(
                "Success", "Welcome to the Student's attendance database"
            )
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="1234", database="login_table"
            )
            my_cur = conn.cursor()
            my_cur.execute(
                "select * from register where email=%s and password = %s",
                (self.txtuser.get(), self.txtpass.get()),
            )

            row = my_cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                Open_main = messagebox.askyesno("YesNo", "Access only for the admin")
                if Open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    

                else:
                    if not Open_main:
                        return

            conn.commit()
            conn.close()

        # ================================ Reset Password ===============================================

    # def reset_pass(self):
    #     if self.combo_security_Q.get() == "Select":
    #         messagebox.showerror("Error", "Select Security Question", parent=self.root2)
    #     elif self.txt_security.get() == "":
    #         messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
    #     elif self.txt_newpass.get() == "":
    #         messagebox.showerror(
    #             "Error", "Please enter the new Password", parent=self.root2
    #         )
    #     else:
    #         conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="login_table")
    #         my_cur = conn.cursor()
    #         qury = ("select * from register where email=%s and securityQ=%s and securityA = %s")
    #         vale = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security)
    #         my_cur.executemany(qury, vale)
    #         # fetching the data from the database and storing it our varible
    #         row = my_cur.fetchone()
    #         print(row)
    #         if row == None:
    #             messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
    #         else:
    #             quer = ("UPDATE register SET password=%s where email=%s")
    #             valu = (self.txt_newpass.get(), self.txtuser.get())
    #             # my_cur.execute(quer, valu)
    #             my_cur.executemany(quer,valu)
                

    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("Info","Your password has been reset, Please login with the New password",parent=self.root2)
    #             # self.root2.destroy()

        # ================================Working on the forget Password ===============================================

    # def forgot_password_window(self):
    #     if self.txtuser.get() == "":
    #         messagebox.showerror(
    #             "Error", "Please enter the email address to reset the password."
    #         )
    #     else:
    #         conn = mysql.connector.connect(
    #             host="localhost", user="root", password="1234", database="login_table"
    #         )
    #         my_cur = conn.cursor()
    #         query = "select * from register where email=%s"
    #         value = (self.txtuser.get(),)
    #         my_cur.execute(query, value)
    #         # This is just to fetch only the email , so we use fetchone
    #         row = my_cur.fetchone()

    #         # If user enter the wrong email for forgetting the password
    #         if row == None:
    #             messagebox.showerror("My Error", "Please enter the valid user name")
    #         else:
    #             conn.close()
    #             self.root2 = Toplevel()
    #             self.root2.title("Forget Password")
    #             self.root2.geometry("380x500+570+180")

    #             l = Label(
    #                 self.root2,
    #                 text="Forget Password",
    #                 font=("times new roman", 23, "bold"),
    #                 fg="red",
    #                 bg="white",
    #             )
    #             l.place(x=0, y=10, relwidth=1)

    #             security_Q = Label(
    #                 self.root2,
    #                 text="Select Security Questions",
    #                 font=("times new roman", 15, "bold"),
    #                 fg="dark green",
    #                 bg="white",
    #             )
    #             security_Q.place(x=35, y=100)

    #             self.combo_security_Q = ttk.Combobox(
    #                 self.root2,
    #                 font=("times new roman", 15, "bold"),
    #                 state="readonly",
    #             )
    #             self.combo_security_Q["values"] = (
    #                 "Select",
    #                 "Your Birth Place",
    #                 "Your Pet name",
    #             )
    #             self.combo_security_Q.place(x=35, y=135, width=285)
    #             self.combo_security_Q.current(0)

    #             security_A = Label(
    #                 self.root2,
    #                 text="Security Answer",
    #                 font=("times new roman", 15, "bold"),
    #                 fg="dark green",
    #                 bg="white",
    #             )
    #             security_A.place(x=35, y=190)

    #             self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
    #             self.txt_security.place(x=35, y=220, width=285)

    #             new_password = Label(
    #                 self.root2,
    #                 text="New Password",
    #                 font=("times new roman", 15, "bold"),
    #                 fg="dark green",
    #                 bg="white")
    #             new_password.place(x=35, y=265)

    #             self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
    #             self.txt_newpass.place(x=35, y=290, width=285)

    #             # ======================Button for resetting the password==========================
    #             btn = Button(
    #                 self.root2,
    #                 text="Reset",
    #                 font=("times new roman", 15, "bold"),
    #                 command=self.reset_pass,
    #                 fg="white",
    #                 bg="green",
    #             )
    #             btn.place(x=130, y=350, width=120, height=35)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==================== Text Variables ==============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ============ Background Image ===============
        self.bg = ImageTk.PhotoImage(
            file=r"images/img7.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        # ================ Main Frame ====================
        frame = Frame(self.root, bg="orange")
        frame.place(x=650, y=0, width=890, height=650)

        # ================ Labels ====================

        register_lbl = Label(
            frame,
            text="__Register Here__",
            font=("times new roman", 35, "bold","italic"),
            fg="red",
            bg="orange",
        )
        register_lbl.place(x=330, y=10)

        # ================ Enteries and Labels =================

        # ========--------------row 1
        fname = Label(
            frame,
            text="First Name",
            font=("times new roman", 17, "bold"),
            fg="black",
            bg="orange",
        )
        fname.place(x=60, y=110)
        # self.text_fname=ttk.Entry(frame,font=("times new roman",15))
        # self.text_fname.place(x=60,y=145,width=285)
        fname_entry = ttk.Entry(
            frame, textvariable=self.var_fname, font=("times new roman", 15)
        )
        fname_entry.place(x=60, y=145, width=285)

        lname = Label(
            frame,
            text="Last Name",
            font=("times new roman", 17, "bold"),
            fg="black",
            bg="orange",
        )
        lname.place(x=545, y=110)
        self.text_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15)
        )
        self.text_lname.place(x=550, y=145, width=285)

        # ========--------------row 2
        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 17, "bold"),
            fg="black",
            bg="orange",
        )
        contact.place(x=57, y=210)
        self.text_contact = ttk.Entry(
            frame, textvariable=self.var_contact, font=("times new roman", 15)
        )
        self.text_contact.place(x=60, y=245, width=285)

        email = Label(
            frame,
            text="Email",
            font=("times new roman", 17, "bold"),
            fg="black",
            bg="orange",
        )
        email.place(x=545, y=210)
        self.text_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15)
        )
        self.text_email.place(x=550, y=245, width=285)

        # ========--------------row 3
        security_Q = Label(
            frame,
            text="Select Security Questions",
            font=("times new roman", 15, "bold"),
            fg="black",
            bg="orange",
        )
        security_Q.place(x=57, y=310)

        self.combo_security_Q = ttk.Combobox(
            frame,
            textvariable=self.var_securityQ,
            font=("times new roman", 15, "bold"),
            state="readonly",
        )
        self.combo_security_Q["values"] = (
            "Select",
            "Your Birth Place",
            "Your Pet name",
        )
        self.combo_security_Q.place(x=60, y=345, width=285)
        self.combo_security_Q.current(0)

        security_A = Label(
            frame,
            text="Security Answer",
            font=("times new roman", 15, "bold"),
            fg="black",
            bg="orange",
        )
        security_A.place(x=545, y=310)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15)
        )
        self.txt_security.place(x=550, y=345, width=285)

        # ========--------------row 4

        pswd = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            fg="black",
            bg="orange",
        )
        pswd.place(x=60, y=405)
        self.txt_pswd = ttk.Entry(
            frame, textvariable=self.var_pass, font=("times new roman", 15)
        )
        self.txt_pswd.place(x=60, y=440, width=285)

        confirm_pswd = Label(
            frame,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            fg="black",
            bg="orange",
        )
        confirm_pswd.place(x=545, y=405)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15)
        )
        self.txt_confirm_pswd.place(x=550, y=440, width=285)

        # +=================== Check Button ============
        self.var_check = IntVar()
        self.check_btn = Checkbutton(
            frame,
            variable=self.var_check,
            text="I am agree with the terms & conditions",
            font=("times new roman", 13, "bold"),
            onvalue=1,
            offvalue=0,
        )
        self.check_btn.place(x=60, y=510)

        # +=================== Button Image =======================
        img = Image.open(
            r"images\btn.png"
        )
        img = img.resize((140, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(
            frame,
            command=self.register_data,
            image=self.photoimage,
            borderwidth=0,
            cursor="hand2",
        )
        b1.place(x=60, y=570, width=140, height=42)

        # +=================== Login Button Image on new User Window  ========================
        img1 = Image.open(
            r"images\login.jpg"
        )
        img1 = img1.resize((140, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(
            frame,
            image=self.photoimage1,
            command=self.return_login,
            borderwidth=0,
            cursor="hand2",
        )
        b2.place(x=600, y=570, width=140, height=42)

    # ======================= Function declaration ==========================
    def register_data(self):
        # If one of the fields are blank or not filled
        if (
            self.var_fname.get() == ""
            or self.var_email.get() == ""
            or self.var_securityQ.get() == "Select"
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        # If our both the passwords are not same
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror(
                "Error", "Both the Passwords must be same", parent=self.root
            )
        elif self.var_check.get() == 0:
            messagebox.showerror(
                "Error",
                "You must need to agree our Terms & conditions.",
                parent=self.root,
            )

        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="1234", database="login_table"
            )
            cur = conn.cursor()
            # validation for not using duplicate emails
            query = "select * from register where email =%s"
            value = (self.var_email.get(),)
            cur.execute(query, value)
            row = cur.fetchone()  # for fetching the data from database
            if row != None:
                messagebox.showerror(
                    "Error", "User with this e-mail already exist", parent=self.root
                )
            else:
                # This will fetch the data from above and put here
                cur.execute(
                    "insert into register values(%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get(),
                    ),
                )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully", parent=self.root)

    # ========================== Login button on the New User window ==============================
    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
