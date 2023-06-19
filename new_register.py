# import imp
import email
from tkinter import *
from tkinter import ttk
from unicodedata import name
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


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
            file=r"images\img7.jpg"
        )
        lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        lbl_bg.place(x=0, y=0, relheight=1, relwidth=1)

        # ================ Main Frame ====================
        frame = Frame(self.root, bg="maroon")
        frame.place(x=650, y=0, width=950, height=650)

        # ================ Labels ====================

        register_lbl = Label(
            frame,
            text="__Register Here__",
            font=("times new roman", 30, "bold", "italic"),
            fg="oliveDrab1",
            bg="maroon",
        )
        register_lbl.place(x=330, y=10)

        # ================ Enteries and Labels =================

        # ========--------------row 1
        fname = Label(
            frame,
            text="First Name",
            font=("times new roman", 17, "bold"),
            fg="chartreuse2",
            bg="maroon",
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
            fg="chartreuse2",
            bg="maroon",
        )
        lname.place(x=555, y=110)
        self.text_lname = ttk.Entry(
            frame, textvariable=self.var_lname, font=("times new roman", 15)
        )
        self.text_lname.place(x=555, y=145, width=285)

        # ========--------------row 2
        contact = Label(
            frame,
            text="Contact No",
            font=("times new roman", 17, "bold"),
            fg="chartreuse2",
            bg="maroon",
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
            fg="chartreuse2",
            bg="maroon",
        )
        email.place(x=555, y=210)
        self.text_email = ttk.Entry(
            frame, textvariable=self.var_email, font=("times new roman", 15)
        )
        self.text_email.place(x=555, y=245, width=285)

        # ========--------------row 3
        security_Q = Label(
            frame,
            text="Select Security Questions",
            font=("times new roman", 15, "bold"),
            fg="chartreuse2",
            bg="maroon",
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
            fg="chartreuse2",
            bg="maroon",
        )
        security_A.place(x=555, y=310)

        self.txt_security = ttk.Entry(
            frame, textvariable=self.var_securityA, font=("times new roman", 15)
        )
        self.txt_security.place(x=555, y=345, width=285)

        # ========--------------row 4

        pswd = Label(
            frame,
            text="Password",
            font=("times new roman", 15, "bold"),
            fg="chartreuse2",
            bg="maroon",
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
            fg="chartreuse2",
            bg="maroon",
        )
        confirm_pswd.place(x=555, y=405)

        self.txt_confirm_pswd = ttk.Entry(
            frame, textvariable=self.var_confpass, font=("times new roman", 15)
        )
        self.txt_confirm_pswd.place(x=555, y=440, width=285)

        # +=================== Check Button ===================
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

        # +=================== Button Image ====
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

        # +=================== Login Image ========================
        img1 = Image.open(
            r"images\login.jpg"
        )
        img1 = img1.resize((140, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=630, y=570, width=140, height=42)

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


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
