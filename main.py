from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
#from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport
from face_recognition import Face_Recognition




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x1080+0+0")
        self.root.title("Face_Recogonition_System")

        #-----------Variables-------------------
       

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Coding\PBL data\Images_GUI\reg1.png")
        img=img.resize((1366,130))
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # backgorund image 
        bg1=Image.open(r"D:\Coding\PBL data\Images_GUI\face-off-banner.jpg")
        bg1=bg1.resize((1366,768))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=350,width=675,height=230)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=210)
        
        b1 = ttk.Button(left_frame, text="Student Pannel",command=self.student_pannels, width=108, style='TButton')
        b1.grid(row=0, column=0)

        
        # Inside the __init__ method, after defining other buttons
        b2 = ttk.Button(left_frame, text="Data Train",command=self.train_pannels, width=108, style='TButton')
        b2.grid(row=1, column=0)

        
        # Inside the __init__ method, after defining other buttons
        b3 = ttk.Button(left_frame, text="Face Detection",command=self.face_recognition, width=108,  style='TButton')
        b3.grid(row=2, column=0)

        
        b4 = ttk.Button(left_frame, text="Photo Sampale", width=108,  style='TButton')
        b4.grid(row=3, column=0)

        
        b5 = ttk.Button(left_frame, text="Attendance",command=self.attendance_pannel, width=108, style='TButton')
        b5.grid(row=4, column=0)
        
        
        b6 = ttk.Button(left_frame, text="developr",command=self.developr, width=108, style='TButton')
        b6.grid(row=5, column=0)
        
        
        b7 = ttk.Button(left_frame, text="HelpSupport",command=self.helpSupport, width=108, style='TButton')
        b7.grid(row=6, column=0)
        
        b8 = ttk.Button(left_frame, text="Exit",command=self.Close, width=108, style='TButton')
        b8.grid(row=7, column=0)
        
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)    
       
    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  
         
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 
    
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window) 
        
    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)           
    
    
    
    def Close(self):
        root.destroy()
        
# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
    
