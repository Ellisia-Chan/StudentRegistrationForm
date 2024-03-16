import tkinter as tk

class MsgBox:
    def __init__(self) -> None:
        pass 

class Window:
    def __init__(self) -> None:
        #Initiate WIndow
        self.win = tk.Tk()
        self.win.title("Student Registrationn")
        self.win.geometry("500x500")
        self.win.resizable(False, False)
        self.win.config(bg="#276FBF")

        #Call Methods to create win contents
        self.frame()
        self.createWidgets()
    def frame(self):
        #Frame
        self.frame1 = tk.Frame(self.win, width=460, height=420, bg="#DED9E2", bd=5, relief=tk.GROOVE)

        #Frame pos
        self.frame1.place(x=20, y=60)

    def createWidgets(self):
        #Vars
        self.radio1 = tk.IntVar()
        menu1, menu2, menu3 = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

        #Window Widgets
        #Label
        lbl_title = tk.Label(self.win, text="Student Registration Form", font=("Arial", 18), bg='#DED9E2')

        #Label pos
        lbl_title.place(x=110, y=20)

        #Frame1 Widgets
        #Label
        lbl_studentName = tk.Label(self.frame1, text="Student Name:", font=("Arial", 16), bg="#DED9E2")
        lbl_studentNumber = tk.Label(self.frame1, text="Student Number:", font=("Arial", 16), bg="#DED9E2")
        lbl_gender = tk.Label(self.frame1, text="Gender", font=("Arial", 16), bg="#DED9E2")
        lbl_gender_others = tk.Label(self.frame1, text="Others:", font=("Arial", 16), bg="#DED9E2")
        lbl_subject = tk.Label(self.frame1, text="Subjects", font=("Arial", 16), bg="#DED9E2")

        #Label pos
        lbl_studentName.place(x=10, y=10)
        lbl_studentNumber.place(x=10, y=50)
        lbl_gender.place(x=180, y=90)
        lbl_gender_others.place(x=30, y=160)
        lbl_subject.place(x=180, y=200)

        #Entry
        ent_studentName = tk.Entry(self.frame1, font=("Arial", 16), width=23)
        ent_studentNunber = tk.Entry(self.frame1, font=("Arial", 16), width=22)
        ent_gender_others = tk.Entry(self.frame1, font=("Arial", 16), width=12)

        #Entry Pos
        ent_studentName.place(x=160, y=10)
        ent_studentNunber.place(x=170, y=50)
        ent_gender_others.place(x=120, y=160)

        #Radiobutton
        rd_btn_female = tk.Radiobutton(self.frame1, text="Female", font=("Arial", 16), bg="#DED9E2", variable=self.radio1, value=1)
        rd_btn_male = tk.Radiobutton(self.frame1, text="Male", font=("Arial", 16), bg="#DED9E2", variable=self.radio1, value=2)
        rd_btn_others = tk.Radiobutton(self.frame1, text="Others", font=("Arial", 16), bg="#DED9E2", variable=self.radio1, value=3)
        
        #Radiobutton pos
        rd_btn_female.place(x=30, y=120)
        rd_btn_male.place(x=180, y=120)
        rd_btn_others.place(x=300, y=120)

        #Checkbutton
        ck_btn_programming2 = tk.Checkbutton(self.frame1, text="Programming 2", font=("Arial", 16), bg="#DED9E2")
        ck_btn_scriptWriting = tk.Checkbutton(self.frame1, text="Scriptwriting and Story Boarding", font=("Arial", 16), bg="#DED9E2")
        ck_btn_FCL3 = tk.Checkbutton(self.frame1, text="FCL 3", font=("Arial", 16), bg="#DED9E2")

        #Checkbutton pos
        ck_btn_programming2.place(x=30, y=230)
        ck_btn_scriptWriting.place(x=30, y=260)
        ck_btn_FCL3.place(x=30, y=290)

        #Button
        btn_proceed = tk.Button(self.frame1, text="Proceed", font=("Arial", 16), bg="#80A1D4", width=15)

        #Button pos
        btn_proceed.place(x=125, y=350)

window = Window()
window.win.mainloop()