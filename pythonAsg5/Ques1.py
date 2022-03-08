#GST Rate Calculator
from tkinter import * # Importing Tkinter module
def calculate(): 
    global gst
    if(paidprice.get().isdecimal()==False):
        gst.set("Invalid Input") 
        g.update() 
    else:
        gstrate = ((float(paidprice.get()) - float(originalcost.get())) * 100) / float(originalcost.get())
        if (gstrate >= 0): #If The gst rate comes positive only then the screen is updated with rate
            gst.set(gstrate)
            g.update()
        else: #Else the screen will show Invalid Input
            gst.set("Invalid Input")
            g.update()

root=Tk() #Creating A New GUI Window
root.geometry("500x500") #Defining Size of GUI Window
l1=Label(text="GST Rate Calculator",font="arial 10 bold") # Defining Heading of The GUI Window
l1.grid(row=0,column=1) #Packing The Label in form of grid
pp1=Label(text="Price Paid:") #Defining Label
pp1.grid(row=1,column=0) #Packing The Label in form of grid
#Creating three String Variable
paidprice=StringVar()
originalcost=StringVar()
gst=StringVar()
#Creating Entry Column
e1=Entry(root,textvariable=paidprice,font="arial 10 bold")
e1.grid(row=1,column=1)
#Creating Label
oc1=Label(text="Original Cost:")
oc1.grid(row=2,column=0) #Packing The Label in form of grid
oc=Entry(root,textvariable=originalcost,font="arial 10 bold") #Creating Entry
oc.grid(row=2,column=1)  #Packing The Label in form of Grid
cal=Button(text="Calculate GST Rate",command=calculate) #Creating a button named Calculate GST Rate
cal.grid(row=3,column=1) #Packing The Label in form of grid
g1=Label(text="GST Rate:")#Creating Label
g1.grid(row=4,column=0)#Packing The Label in form of grid
g=Entry(root,textvariable=gst,font="arial 10 bold")#Creating Label
g.grid(row=4,column=1)#Packing The Label in form of grid
root.mainloop()
