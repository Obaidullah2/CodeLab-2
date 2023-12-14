#Exercise 2: Managing Layout 
#Exercise 2 a: Using pack 
#Create a GUI with 4 labels using the pack() geometry as shown in the below images. The first image on the left shows the original display and the second image on right shows what happens when the window is resized.


#Additional information:Arguments values for many widgets, including Frames for Borders and Background

#bd is used for border width. For example bd=5
#Relief is used for border-style values are FLAT, RAISED, GROOVE, SUNKEN, and RIDGE. For example relief=RAISED
#bg is used for background color.For example bg="white" or bg="#FFFFFF".
#Pack arguments

#Fill: Fill the space with the widget, Values are Y, X, BOTH. For example fill=Y
#Expand: The size of the button is expanded if the window is maximized. Values are 0,1, any number, YES, NO. For example expand=0 (default) no expansion


from tkinter import *
import random
app=Tk()
app.title("GUI Example 4")
bA = Label(app,text="A",width=12,bg='red',relief=GROOVE,bd=5)
bB = Label(app,text="B",width=12,bg='yellow')
bC = Label(app,text="C",width=12,bg='blue')
bD = Label(app,text="D",width=12,bg='white')
bA.pack(side='top',fill=X,expand=1)
bB.pack(side='bottom')
bC.pack(side='left',fill=Y,expand=1)
bD.pack(side='right')
app.mainloop()

