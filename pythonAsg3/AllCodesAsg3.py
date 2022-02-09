#Ques 1
enteredString=str(input("Enter The String : "))

#if space " " is present 
if " " in enteredString:
    #we will check frequency of words
    freq1=dict()
    words=enteredString.split() 
    #traversing list of words
    for word in words:
        if word in freq1:
            freq1[word]=freq1[word]+1
        else:
            freq1[word]=1
    for freq in freq1:
        print(freq,freq1[freq])

# if no space means singal word
else:
    #we will check frequency of alphabets
    freq2=dict()
    
    for letter in enteredString:
        if letter in freq2:
            freq2[letter]=freq2[letter]+1
        else:
            freq2[letter]=1
    for freq in freq2:
        print(freq,freq2[freq])

#Ques 2

#  conditions for leap year
#   leap year if perfectly divisible by 400
# not leap year if perfectly divisible by 100
# leap if ND by 100 and 400 but divisible by 4

day=int(input("DAY: "))
month=int(input("MONTH: "))
year=int(input("YEAR: "))

if year%400==0:
    a=1
    #leap year

elif year%4==0 and year%100!=0 :
    a=1
    #leap year

else :
    a=2
    #not leap year
if day<=31 and month<=12:
    # 31 days months are 1 3 5 7 8 10 12
    if  month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day==31:
            day=1
            if month==12:
                month=1
                year=year+1
            else:
                month=month +1
        else:
            day=day+1
    # if leap year
    elif a==1:
        if month==2 and day==28:
            day=29
        elif month==2 and day==29 :
            day=1
            month=3
        else:
            if day==30:
                day=1
                month=month +1
            else:
                day=day+1
    #if not leap year
    elif a==2:
        if month==2 and day==28 :
            day=1
            month=3
        else:
            if day==30:
                day=1
                month=month +1
            else:
                day=day+1


    if month==4 or month==6 or month==11 or month==9:
        if day==31 or day==32:
            print("This day is not valid")
        else:
            print("Next Date is:",  day,"/",month,"/",year)

    elif a==2 and month ==2 and day>=29:
        print("This day is not valid")     
    else:
        print("Next Date is:",  day,"/",month,"/",year)

else:
    print("This is not a valid date")



#Ques 3

list1=[3,9,10]
list2=[]
for i in list1:
   list2.append((i,i**2))
print(list2)

#Ques 4

i=1
#keep entering grade untill valid grade is entered
while i>0:

    grade=int(input("Enter Your Grade : "))
    if grade<4 or grade>10:
        print("Enter Valid Grade")
    else:
        i-=1

grades=["A+","A","B+","B","C+","C","D"]
performances=["Outstanding","Excellent","Very Good","Good","Average","Below Average","Poor"]

print("Your Grade Is ",grades[10-grade]," And ",performances[10-grade], " Perfornmance.")


#Ques 5


x=0
for j in range(0,6):
    print(" "*j,end="")
    i=65
    for i in range(65,76) :
        if i==76-x:
            break
        print(chr(i),end="")   # using ASCII values and typecasting
    x=x+2
    print(" ")

    #Ques  6
student_info=dict()
n="y"
alistsid=[]

#(a)
#here we keep a while loop that goes for infinite times
#hence it asks sid and names repeatedly and adds them to dictionary
#here i have used the if statement so that i can exit the loop whenever i want
#i am making a list along with the dictionary which will help us in further parts
print("----------------(a)-------------------")
while(n=="y"):
    sid=int(input("Give the sid (a number):"))
    name=input("Enter your name:")
    student_info[sid]=name
    n=input("give a letter y or n:")
    alistsid.append((sid,name))
print("The required dictionary--",student_info)
print("The list will be used in further parts--")
print("The required list--",alistsid)

#(b)
#to sort our dictionary based to names we will iterate dict.items() twice each
#time inversing the key value pair and we will form a list which can be sorted
#and converted back to dictionary hence we get the required dictionary
print("----------------(b)------------------------")
print("The dictionary we had-")
print(student_info)
#now we exchange the key value pair and make a new dictionary and a new list
newdict=dict()
alistname=[]
#now we iterate
for (k,v) in student_info.items():
    newdict[v]=k
    alistname.append((v,k))
print("now we have exchanged the key value pair but its not sorted-")
#our dict and list are both not sorted
print(newdict)
print("The unsorted list--")
print(alistname)
alistname.sort()
#sorted list
print("The sorted list--")
print(alistname)
#now we create a sorted dictionary from our sorted list
print("The sorted dictionary-")
sorted_dict=dict(alistname)
print(sorted_dict)
#now we just need to exchange the key value pair of the sorted_dict to get
#our required dictionary
required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("This is the dictionary sorted on the basis of name-")
print(required_dict_name)

#(c)
#sort the dictionary on the basis of sid
#the list we made along with dictionary will be used now
#we will first sort the list and then convert it into dictionary 
print("-----------------(c)-----------------")
print("The list we made before will be used now-")
print(alistsid)
alistsid.sort()
print("now the list is sorted-")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid-",sorted_student_info_sid)

#(d)
#search a student's name by his/her sid
#here i will search the name of the student with key value or sid as 21103105    
print("-----------------(d)-----------------")    
entered_sid=int(input("Please enter one of the sids you entered before-"))
print("The name of the student with the entered sid is-")    
print(student_info[entered_sid])


    #Ques 7

numOfElements=int(input("Enter the Number Of Elements : "))
#fibonacci series 0 1 1 2 3 5 8 13...
prev=0
next=1
sum=0
if numOfElements>=1:
    print(prev," ")
    sum=sum+prev
if numOfElements>=2:
    print(next," ")
    sum=sum+next
while numOfElements>2:
    a= prev + next
    sum=sum+a
    print(a," ")
    prev=next
    next=a
    numOfElements=numOfElements-1

print("Average of This Fibonacci series is : ",sum/numOfElements)

#Ques 8

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#part a
print("part a")
Set4=(Set1 ^ Set2)
print(Set4)

#part b
print("part b")
Set5= Set1 ^ (Set2 ^ Set3)
print(Set5)#empty

#part c
print("part c")
Set6 =((Set1 & Set2)|(Set2 & Set3)|(Set1 & Set3))-Set5
print(Set6)

#part d
print("part d")
ls=[]
for i in range(1,10):
  if i not in Set1:
      ls.append(i)
Set7=set(ls)
print(Set7)
#part e
print("part e")
ls2=[]
for i in range(1,10):
  if i not in Set1 and i not in Set2 and i not in Set3:
    ls2.append(i)
Set8=set(ls2)
print(Set8)
