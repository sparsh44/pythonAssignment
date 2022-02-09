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
