from tkinter import * 
import calendar #Importing Calendar Module

root=Tk()
def cshow(): #cal1 function is defined
    global year
    new=Tk() # A New GUI is created
    new.geometry("600x700") #Defining Size of GUI Window
    l1=Label(new,text=(calendar.calendar(int(year.get()))), font = "arial 10 bold") #Creating Label
    l1.grid(row=0,column=0,padx=30)#Packing The Label in form of grid and padding it in X Axis
    new.mainloop()
root.geometry("500x500")

heading=Label(text="Calendar",font="arial 10 bold")
heading.place(x=80,y=1)#Using place to pack the label
year1=Label(text="Enter Year: ")#Creating Label
year1.place(x=0,y=30)#Using place to pack the label
year=StringVar() #Creating String Variable
e2=Entry(root,textvariable=year) # Creating Entry Label
e2.place(x=60,y=30) #Using place to pack the label

cal=Button(text="Show Calendar",command=cshow) #Creating Button
cal.place(x=60,y=50) #Packing The button using place function


root.mainloop()