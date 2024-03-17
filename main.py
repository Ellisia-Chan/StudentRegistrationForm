import tkinter as tk
from tkinter import messagebox
class MsgBox:
    def __init__(self, widget_value):
        #Access widgets from another class
        self.window_widgets = widget_value

        #vars
        self.name = ""
        self.number = ""
        self.gender = ""
        self.gender_others = ""
        self.subject_txt = ""

    def getInfo(self):
        #Get Student Name and Student Number
        self.name = self.window_widgets.ent_studentName.get()
        self.number = self.window_widgets.ent_studentNumber.get()
        
        #Get Student Gender
        if self.window_widgets.radio1.get() == 1:
            self.gender = "Female"
        elif self.window_widgets.radio1.get() == 2:
            self.gender = "Male"
        elif self.window_widgets.radio1.get() == 3:
            self.gender = self.window_widgets.ent_gender_others.get()

        #Get Subjects
        if self.window_widgets.menu1.get() == True:
            self.subject_txt += "Programming 2\n"

        if self.window_widgets.menu2.get() == True:
            self.subject_txt += "Scriptwriting and Story Boarding\n"

        if self.window_widgets.menu3.get() == True:
            self.subject_txt += "FCL 3\n"

        #Create MsgBpox
        self.createMsgBox()

        #Debugging
        # print(self.name)
        # print(self.number)
        # print(self.gender)
        # print(self.subject_txt)

    def createMsgBox(self):
        msg = f"Student Name: {self.name}\nStudent Number: {self.number}\nGender: {self.gender}\nSubjects: \n{self.subject_txt}"
        messagebox.showinfo("Student Registration Form", msg)

    def clear(self):
        #Return to Default Value
        self.name = ""
        self.number = ""
        self.gender = ""
        self.gender_others = ""
        self.subject_txt = ""

        #Delete Values in Entry Field
        self.window_widgets.ent_studentName.delete(0, tk.END)
        self.window_widgets.ent_studentNumber.delete(0, tk.END)

        self.window_widgets.radio1.set(-1)
        self.window_widgets.ck_btn_programming2.deselect()
        self.window_widgets.ck_btn_scriptWriting.deselect()
        self.window_widgets.ck_btn_FCL3.deselect()

        self.window_widgets.lbl_gender_others.place_forget()
        self.window_widgets.ent_gender_others.delete(0, tk.END)
        self.window_widgets.ent_gender_others.place_forget()

class Window:
    def __init__(self):
        #Access widgets to another class
        self.msgbox = MsgBox(self)
        #Initiate WIndow
        self.win = tk.Tk()
        self.win.title("Student Registrationn")
        self.win.geometry("500x500")
        self.win.resizable(False, False)
        self.win.config(bg="#276FBF")

        #Call methods to create win contents
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
        self.menu1, self.menu2, self.menu3 = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()

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
        self.lbl_gender_others = tk.Label(self.frame1, text="Others:", font=("Arial", 16), bg="#DED9E2")
        lbl_subject = tk.Label(self.frame1, text="Subjects", font=("Arial", 16), bg="#DED9E2")

        #Label pos
        lbl_studentName.place(x=10, y=10)
        lbl_studentNumber.place(x=10, y=50)
        lbl_gender.place(x=180, y=90)
        self.lbl_gender_others.place_forget()
        lbl_subject.place(x=180, y=200)

        #Entry
        self.ent_studentName = tk.Entry(self.frame1, font=("Arial", 16), width=23)
        self.ent_studentNumber = tk.Entry(self.frame1, font=("Arial", 16), width=22)
        self.ent_gender_others = tk.Entry(self.frame1, font=("Arial", 16), width=14)

        #Entry Pos
        self.ent_studentName.place(x=160, y=10)
        self.ent_studentNumber.place(x=170, y=50)
        self.ent_gender_others.place_forget()

        #Radiobutton
        rd_btn_female = tk.Radiobutton(self.frame1, text="Female", font=("Arial", 16), bg="#DED9E2", activebackground="#DED9E2",
                                       variable=self.radio1, value=1, command=self.showHideGenderOthers)
        rd_btn_male = tk.Radiobutton(self.frame1, text="Male", font=("Arial", 16), bg="#DED9E2", activebackground="#DED9E2", 
                                     variable=self.radio1, value=2, command=self.showHideGenderOthers)
        rd_btn_others = tk.Radiobutton(self.frame1, text="Others", font=("Arial", 16), bg="#DED9E2", activebackground="#DED9E2", 
                                       variable=self.radio1, value=3, command=self.showHideGenderOthers)
        
        #Radiobutton pos
        rd_btn_female.place(x=30, y=120)
        rd_btn_male.place(x=180, y=120)
        rd_btn_others.place(x=300, y=120)

        #Checkbutton
        self.ck_btn_programming2 = tk.Checkbutton(self.frame1, text="Programming 2", font=("Arial", 16), 
                                             bg="#DED9E2", activebackground="#DED9E2", variable=self.menu1)
        self.ck_btn_scriptWriting = tk.Checkbutton(self.frame1, text="Scriptwriting and Story Boarding", font=("Arial", 16), 
                                              bg="#DED9E2", activebackground="#DED9E2", variable=self.menu2)
        self.ck_btn_FCL3 = tk.Checkbutton(self.frame1, text="FCL 3", font=("Arial", 16), bg="#DED9E2", activebackground="#DED9E2", variable=self.menu3)

        #Checkbutton pos
        self.ck_btn_programming2.place(x=30, y=230)
        self.ck_btn_scriptWriting.place(x=30, y=260)
        self.ck_btn_FCL3.place(x=30, y=290)

        #Button
        btn_proceed = tk.Button(self.frame1, text="Proceed", font=("Arial", 16), bg="#F7F4EA", 
                                activebackground="#8DA9C4", width=15, command=self.msgbox.getInfo)
        btn_clear = tk.Button(self.frame1, text="Clear Forms", font=("Arial", 8), bg="#F7F4EA", 
                              activebackground="#8DA9C4", width=10, command=self.msgbox.clear)

        #Button pos
        btn_proceed.place(x=125, y=350)
        btn_clear.place(x=5, y=380)
    
    def showHideGenderOthers(self):
        if self.radio1.get() == 3:
            self.lbl_gender_others.place(x=30, y=160)
            self.ent_gender_others.place(x=120, y=160)
        else:
            self.lbl_gender_others.place_forget()
            self.ent_gender_others.delete(0, tk.END)
            self.ent_gender_others.place_forget()
            
            
window = Window()
window.win.mainloop()