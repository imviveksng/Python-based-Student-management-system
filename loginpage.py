from tkinter import *
import ttkthemes
from tkinter import ttk
import time
from tkinter import messagebox as mg
from PIL import ImageTk
#window for display
vivek=ttkthemes.ThemedTk()
vivek.get_themes()
vivek.set_theme('radiance')
vivek.title('Login Page')
vivek.geometry('1200x700')
vivek.resizable(0,0)
background=ImageTk.PhotoImage(file='test4.jpg')
bgLabel=Label(vivek,image=background)
bgLabel.place(x=0,y=0)

#functionality Part
def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date:{date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)
#creating datetime label
datetimeLabel=Label(vivek,font=('arial',15,'bold'))
datetimeLabel.place(x=5,y=5)
clock() 
#for username,password and importing another py file
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        mg.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get()=='vivek'or'amit'or'revanth'or 'akash' or'abhishek' and passwordEntry.get()=='1234' or '0000': 
        mg.showinfo('Success','Welcome! Vivek') 
        vivek.destroy()  
        import studentmanage
        
    else:
        mg.showerror('Error','Please enter correct credentials')    
#login frame
loginFrame=Frame(vivek,bg="seashell")
loginFrame.place(x=330,y=100)
logoImage=PhotoImage(file='student.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
#username label
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('Arial',20,'bold'),bg='seashell')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('Libre Baskerville',20,'bold'),bd=5,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)
#password label
passwordImage=PhotoImage(file='padlock.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('Arial',20,'bold'),bg='seashell')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('Libre Baskerville',20,'bold'),bd=5,fg='black',show="*")
passwordEntry.grid(row=2,column=1,pady=10,padx=20)
#login button
loginButton=ttk.Button(loginFrame,text='Login',width=10,cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=5)

vivek.mainloop()
