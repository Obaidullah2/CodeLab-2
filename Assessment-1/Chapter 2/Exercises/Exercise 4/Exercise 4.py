#Exercise 4: Registration page 
#Using widgets create a GUI as shown in below image



# importing the tkinter module library
from tkinter import *

# imported the os library to help with the file paths in the os
import os

# importing the PIL library (photo imaging library), as python does not support images with png format
from PIL import ImageTk, Image

# creating a variable, for the application window
app = Tk()

# setting the title, dimensions, resizable options for the application window
app.title("Registration Page")
app.geometry("600x750")
app.resizable(1, 1)
# setting the background color
app.configure(background = '#ffffff')


## CREATING FUNCTIONS FOR THE BUTTONS 

# creating a function for the cancel button
def cancel():
    stdtext.delete(0, "end")
    mobilenumtext.delete(0, "end")
    email_idbox.delete(0, "end")
    homeaddressbox.delete(0, "end")
    genderdisplay_optn.set("")
    courses_radios.set("")
    eng_check.set(False)
    tagalog_check.set(False)
    urdu_check.set(False)


# creating a function for the submit button
def submit():
    stdtext.get()
    mobilenumtext.get()
    email_idbox.get()
    homeaddressbox.get()
    genderdisplay_optn.get()
    courses_radios.get()
    eng_check.get()
    tagalog_check.get()
    urdu_check.get()

    smallwindow = Tk()

    smallwindow.title("Success")
    smallwindow.geometry("150x75")
    smallwindow.resizable(0, 0)

    msg = Label(smallwindow, text = "Details Submitted")
    msg.pack()
    

##CREATING ALL THE REQUIRED WIDGETS/LABELS 

# creating a frame to place all the tabs inside the frame
main_frame = LabelFrame(app, width = 400, height = 725, bg = '#d3d3d3', border = 0)

# creating a sub frame for the label and entry widgets
sub_frame = LabelFrame(main_frame, width = 500, height = 700, bg = '#d3d3d3', border = 0)

# creating a label as the main heading inside the main frame
main_head = Label(main_frame, font = ('Roboto', 18, 'bold'), text = "Student Managemnet System", bg = '#d3d3d3')

# creating a sub-heading inside the frame
subhead = Label(main_frame, font = ('Roboto', 14), text = "New Student Registration", bg = '#d3d3d3')

# adding the image inside a label with the university logo at the top
scriptdir = os.path.dirname(os.path.realpath(__file__))         
banner = Image.open(os.path.join(scriptdir, "BSULOGO.png"))    
logobsubanner = ImageTk.PhotoImage(banner)                      
imglabel = Label(app, image = logobsubanner, height = 130)      
# app.geometry(f"{banner.width}x700") 

# creating the student name text label and the text box for the student name 
stdname = Label(sub_frame, font = ('Roboto', 12), text = "Student Name", bg = '#d3d3d3')
stdtext = Entry(sub_frame, width = 25, font = ('Roboto', 12))

# creating the mobile number text label and a text box for it
mobilenum = Label(sub_frame, font = ('Roboto', 12), text = "Mobile Number", bg = '#d3d3d3')
mobilenumtext = Entry(sub_frame, width = 25, font = ('Roboto', 12))

# creating the label and text box for email id
email_id = Label(sub_frame, font = ('Roboto', 12), text = "Email ID", bg = '#d3d3d3')
email_idbox = Entry(sub_frame, width = 25, font = ('Roboto', 12))

# creating the label and text box for home address
homeaddress = Label(sub_frame, font = ('Roboto', 12), text = "Home Address", bg = '#d3d3d3')
homeaddressbox = Entry(sub_frame, width = 25, font = ('Roboto', 12))

# creating the label and text box for the gender
gender = Label(sub_frame, font = ('Roboto', 12), text = "Gender", bg = '#d3d3d3')

genderdisplay_optn = StringVar()
genderdisplay = ['Select', 'Male', 'Female', 'Rather not Say']
genderdrop = OptionMenu(sub_frame, genderdisplay_optn, *genderdisplay)
genderdisplay_optn.set(genderdisplay[0])

# creating a label and radio buttons for courses enrolled
coursesenrolled = Label(sub_frame, font =('Roboto', 12), text = "Course Enrolled", bg = '#d3d3d3')

courses_radios = StringVar(value = 0)
# radio buttons
course_rd1 = Radiobutton(sub_frame, text = "BSc CC", bg = '#d3d3d3', font = ('Roboto', 9), variable = courses_radios, value = 1)    # radio button 1 
course_rd2 = Radiobutton(sub_frame, text = "BSc CY", bg = '#d3d3d3', font = ('Roboto', 9), variable = courses_radios, value = 2)    # radio button 2
course_rd3 = Radiobutton(sub_frame, text = "BSc PSY", bg = '#d3d3d3', font = ('Roboto', 9), variable = courses_radios, value = 3)   # radio button 3
course_rd4 = Radiobutton(sub_frame, text = "BA & BM", bg = '#d3d3d3', font = ('Roboto', 9), variable = courses_radios, value = 4)   # radio button 4

# creating a label and checkboxes for the languages known option
languages = Label(sub_frame, font = ('Roboto', 12), text = "Languages known", bg = '#d3d3d3')

# checkboxes
checkbox1 = Checkbutton(sub_frame, text = 'English', bg = '#d3d3d3', font = ('Roboto', 9))
eng_check = BooleanVar()

checkbox2 = Checkbutton(sub_frame, text = 'Tagalog', bg = '#d3d3d3', font = ('Roboto', 9))
tagalog_check = BooleanVar()

checkbox3 = Checkbutton(sub_frame, text = 'Hindi/Urdu', bg = '#d3d3d3', font = ('Roboto', 9))
urdu_check = BooleanVar()

# creating the text message and its progress meter
rates = Label(sub_frame, font = ('Roboto', 10, 'bold'), text = "Rate your English communication skills", bg = '#d3d3d3')
progressmeter = Scale(sub_frame, from_ = 0, to = 100, orient = HORIZONTAL, width = 40, troughcolor = '#ffffff')


# creating the two buttons (submit and clear)
submit_btn = Button(sub_frame, font = ('Roboto', 10), text = "Submit", bg = '#1a2b4c', padx = 5, pady = 5,fg = '#ffffff', command = submit)   # submit button
clear_btn = Button(sub_frame, font = ('Roboto', 10), text = "Clear", bg = '#1a2b4c', padx = 5, pady = 5,fg = '#ffffff', command = cancel)     # clear button



##PACKING ALL THE REQURED ITEMS 

imglabel.pack(side = TOP)                                         
main_frame.pack(side = TOP, pady = 10)                            
main_head.pack(side =  TOP, padx = 10, pady = 5)           
subhead.pack(side = TOP, padx = 5, pady = 5)                     
sub_frame.pack(side = TOP, padx = 5, pady = 5)                   
stdname.grid(row = 0, column = 0, pady = 5)                      
stdtext.grid(row = 0, column = 1, pady = 5)                       
mobilenum.grid(row = 1, column = 0, pady = 5)                     
mobilenumtext.grid(row = 1, column = 1, pady = 5)                 
email_id.grid(row = 2, column = 0, pady = 5)                      
email_idbox.grid(row = 2, column = 1, pady = 5)                   
homeaddress.grid(row = 3, column = 0, pady = 5)                   
homeaddressbox.grid(row = 3, column = 1, pady = 5)                
gender.grid(row  = 4, column = 0, pady = 5)                       
genderdrop.grid(row = 4, column = 1, pady = 5)                    
coursesenrolled.grid(row = 5, column = 0, pady = 5)               

# packing all the radio buttons
course_rd1.grid(row = 5, column = 1, pady = 5)                    # course radio button 1
course_rd2.grid(row = 6, column = 1, pady = 5)                    # course radio button 2  
course_rd3.grid(row = 7, column = 1, pady = 5)                    # course radio button 3  
course_rd4.grid(row = 8, column = 1, pady = 5)                    # course radio button 4

languages.grid(row = 9, column = 0, pady = 5)                    # packing the languages label inside the mainframe

# packing all the checkboxes
checkbox1.grid(row = 9, column = 1, pady = 5)                    # language 1
checkbox2.grid(row = 9, column = 2, pady = 5)                    # language 2
checkbox3.grid(row = 10, column = 1, pady = 5)                   # language 3

rates.grid(row = 11, column = 0, pady = 5)                      
progressmeter.grid(row = 11, column = 1, pady = 5)               

submit_btn.grid(row = 12, column = 0, padx = 10,pady = 5)        
clear_btn.grid(row = 12, column = 1, padx = 10,pady = 5)         


# using the mainloop function to run the window...
app.mainloop()
