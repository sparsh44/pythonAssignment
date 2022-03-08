from tkinter import *

def b0i(): #Creating a function to add 0 in String Variable
    global ent
    ent.set(ent.get()+'0') #Adding 0 to the string
    inoutvar.update() #Updating the screen
def b1i(): #Creating a function to add 1 in String Variable
    global ent
    ent.set(ent.get()+'1') #Adding 1 to the string
    inoutvar.update() #Updating the screen
def b2i(): #Creating a function to add 2 in String Variable
    global ent
    ent.set(ent.get()+'2')#Adding 2 to the string
    inoutvar.update() #Updating the screen
def b3i(): #Creating a function to add 3 in String Variable
    global ent
    ent.set(ent.get()+'3')#Adding 3 to the string
    inoutvar.update() #Updating the screen
def b4i(): #Creating a function to add 4 in String Variable
    global ent
    ent.set(ent.get()+'4')#Adding 4 to the string
    inoutvar.update() #Updating the screen
def b5i(): #Creating a function to add 5 in String Variable
    global ent
    ent.set(ent.get()+'5')#Adding 5 to the string
    inoutvar.update() #Updating the screen
def b6i(): #Creating a function to add 6 in String Variable
    global ent
    ent.set(ent.get()+'6')#Adding 6 to the string
    inoutvar.update() #Updating the screen
def b7i(): #Creating a function to add 7 in String Variable
    global ent
    ent.set(ent.get()+'7')#Adding 7 to the string
    inoutvar.update() #Updating the screen
def b8i(): #Creating a function to add 8 in String Variable
    global ent
    ent.set(ent.get()+'8')#Adding 8 to the string
    inoutvar.update() #Updating the screen
def b9i(): #Creating a function to add 9 in String Variable
    global ent
    ent.set(ent.get()+'9')#Adding 9 to the string
    inoutvar.update() #Updating the screen
def clear(): #Creating the clear function to clear the string
    global ent
    ent.set("")
    inoutvar.update() #Update the Screen
def equal():
    global ent
    variable=eval(inoutvar.get()) #Creating A Variable and using eval function to calculate the value
    ent.set(variable) #Setting the String
    inoutvar.update() #Update the screen


def plus(): #Creating a function to add plus in string
    global ent
    ent.set(ent.get() + '+')#Setting the String
    inoutvar.update()#Update the screen

def sub():#Creating a function to add subtract in string
    global ent
    ent.set(ent.get()+'-')#Setting the String
    inoutvar.update()#Update the screen


def mul(): #Creating a function to add multiply in string
    global ent
    ent.set(ent.get() + '*') #Setting the String
    inoutvar.update()#Update the screen


def div(): #Creating a function to add division in string
    global ent
    ent.set(ent.get() + '/') #Setting the String
    inoutvar.update() #Update the screen


root=Tk()
root.geometry("500x500") #Defining Size of GUI Window
label1=Label(text="Calculator",font="arial 20 bold") #Creating Label
label1.pack(padx=20) #Packing the Label
ent=StringVar() #Creating a String Variable
inoutvar=Entry(textvariable=ent,font="arial 30 bold") #Creating a Entry Column
inoutvar.pack(padx=20) #Packing the entry column and padding it

button0=Button(text="0",padx=20, command=b0i,font="arial 14 bold") #Creating a button named 0 and given a command to add 0 in the string
button0.place(x=160,y=220) #Placing it at (160,220)
button1=Button(text="1",padx=20, command=b1i,font="arial 14 bold")#Creating a button named 1 and given a command to add 1 in the string
button1.place(x=80,y=100) #Placing it at (80,100)
button2=Button(text="2",padx=20, command=b2i,font="arial 14 bold")#Creating a button named 2 and given a command to add 2 in the string
button2.place(x=160,y=100)#Placing it at (160,100)
button3=Button(text="3",padx=20, command=b3i,font="arial 14 bold")#Creating a button named 3 and given a command to add 3 in the string
button3.place(x=240,y=100)#Placing it at (240,100)
button4=Button(text="4",padx=20, command=b4i,font="arial 14 bold")#Creating a button named 4 and given a command to add 4 in the string
button4.place(x=80,y=140)#Placing it at (80,140)
button5=Button(text="5",padx=20, command=b5i,font="arial 14 bold")#Creating a button named 5 and given a command to add 5 in the string
button5.place(x=160,y=140)#Placing it at (160,140)
button6=Button(text="6",padx=20, command=b6i,font="arial 14 bold")#Creating a button named 6 and given a command to add 6 in the string
button6.place(x=240,y=140)#Placing it at (240,140)
button7=Button(text="7",padx=20, command=b7i,font="arial 14 bold")#Creating a button named 7 and given a command to add 7 in the string
button7.place(x=80,y=180)#Placing it at (80,180)
button8=Button(text="8",padx=20, command=b8i,font="arial 14 bold")#Creating a button named 8 and given a command to add 8 in the string
button8.place(x=160,y=180)#Placing it at (160,180)
button9=Button(text="9",padx=20, command=b9i,font="arial 14 bold")#Creating a button named 9 and given a command to add 9 in the string
button9.place(x=240,y=180)#Placing it at (240,180)
buttonplus=Button(text="+",padx=20, command=plus,font="arial 14 bold")#Creating a button named + and given a command to add + in the string
buttonplus.place(x=80,y=260,width=67)#Placing it at (80,260)
buttonsub=Button(text="-",padx=20, command=sub,font="arial 14 bold")#Creating a button named - and given a command to add - in the string
buttonsub.place(x=160,y=260,width=67)#Placing it at (160,260)
buttonmul=Button(text="X",padx=20, command=mul,font="arial 14 bold")#Creating a button named X and given a command to add X in the string
buttonmul.place(x=240,y=260,width=67)#Placing it at (240,260)
buttondiv=Button(text="/",padx=20, command=div,font="arial 14 bold")#Creating a button named / and given a command to add / in the string
buttondiv.place(x=80,y=300,width=67)#Placing it at (80,300)
buttonequal=Button(text="=",padx=20, command=equal,font="arial 14 bold")#Creating a button named = and given a command to evaluate and update the string
buttonequal.place(x=160,y=300,width=67)#Placing it at (160,300)
buttonclear=Button(text="C",padx=20, command=clear,font="arial 14 bold")#Creating a button named C and given a command to clear the string
buttonclear.place(x=240,y=300,width=67)#Placing it at (240,300)
root.mainloop()
 