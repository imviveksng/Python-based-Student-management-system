import datetime
import ttkthemes
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3 

# Creating the universal font variables
headlabelfont = ("Dubai Medium", 16, 'bold')
labelfont = ('Aptos Display', 14)
entryfont = ('Aptos Display', 12)
# Connecting to the Database where all information will be stored
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT)"
)
# Creating the functions

def reset_fields():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
   for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
       exec(f"{i}.set('')")
   dob.set_date(datetime.datetime.now().date())
def reset_form():
   global tree
   tree.delete(*tree.get_children())
   reset_fields()
def display_records():
    tree.delete(*tree.get_children())
    curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
    data = curr.fetchall()
    for record in data:
        tree.insert('', END, values=record)
def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
    name = name_strvar.get().upper()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get().upper()
    DOB = dob.get_date()
    stream = stream_strvar.get().upper()
    if not name or not email or not contact or not gender or not DOB or not stream:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    elif len(contact) != 10 or not contact.isdigit():
        mb.showerror('Error!', "Please enter a 10-digit phone number")
    else:
        try:
            connector.execute(
                'INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)',
                (name, email, contact, gender, DOB, stream)
            )
            connector.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
            reset_fields()
            display_records()
        except:
            mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')

def remove_record():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       connector.execute('DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
       connector.commit()
       mb.showinfo('Done', 'The record you wanted delete was successfully deleted.')
       display_records()
def view_record():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar
   if not tree.selection():
       mb.showerror('Error!', 'Please select a record to view')
   else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]
        
        name_strvar.set(selection[1]); email_strvar.set(selection[2])
        contact_strvar.set(selection[3]); gender_strvar.set(selection[4])
        date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
        dob.set_date(date);stream_strvar.set(selection[6])


# Initializing the GUI window
main=ttkthemes.ThemedTk()
main.get_themes()
main.set_theme('keramik')
main.title(' School Management System by विवेक सिंह')
main.geometry('1200x700')
main.resizable(1, 1)

# Creating the background and foreground color variables
lf_bg = 'skyblue2' # bg color for the left_frame
cf_bg = 'skyblue' # bg color for the center_frame
# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()
#Using slider performing slide of characters
count=0
text=' '
def slider():
    global text,count
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(0,slider)
# Placing the components in the main window
s='STUDENT MANAGEMENT SYSTEM' 
sliderLabel=Label(main,text=s,font=headlabelfont,bg='white')   
sliderLabel.place(x=500,y=-1)
slider()
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)
# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.05)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.18)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.31)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.44)
Label(left_frame, text="Date of Birth (DOB)", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)
Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.7)
Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.36)

OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.49, relwidth=0.5)
OptionMenu(left_frame, stream_strvar, 'BCA','MCA','BBA','BCOM').place(x=45, rely=0.75, relwidth=0.5)
dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=20, rely=0.62)
d=ttk.Button(left_frame, text='Submit and Add Record',  command=add_record,cursor='hand2', width=35).place(relx=0.025, rely=0.85)
# Placing components in the center frame
a=ttk.Button(center_frame, text='Delete Record', command=remove_record,cursor='hand2', width=15).place(relx=0.1, rely=0.25)
b=ttk.Button(center_frame, text='View Record',  command=view_record,cursor='hand2', width=15).place(relx=0.1, rely=0.35)
c=ttk.Button(center_frame, text='Reset Fields',  command=reset_fields,cursor='hand2', width=15).place(relx=0.1, rely=0.45)
d=ttk.Button(center_frame, text='Delete database',  command=reset_form,cursor='hand2', width=15).place(relx=0.1, rely=0.55)
# Placing components in the right frame
Label(right_frame, text='Students Records', font=headlabelfont, bg='cadet blue', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE, show='headings')
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.column('#0', width=0, minwidth=0, stretch=NO)
tree.column('#1', width=40, minwidth=40, stretch=NO, anchor=CENTER)
tree.column('#2', width=140, minwidth=140, stretch=NO, anchor=CENTER)
tree.column('#3', width=200, minwidth=200, stretch=NO, anchor=CENTER)
tree.column('#4', width=80, minwidth=80, stretch=NO, anchor=CENTER)
tree.column('#5', width=80, minwidth=80, stretch=NO, anchor=CENTER)
tree.column('#6', width=80, minwidth=80, stretch=NO, anchor=CENTER)
tree.column('#7', width=150, minwidth=150, stretch=NO, anchor=CENTER)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()
# Finalizing the GUI window
main.update()
main.mainloop()