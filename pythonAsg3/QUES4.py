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
