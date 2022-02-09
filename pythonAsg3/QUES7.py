"""Write a python program to print Fibonacci sequence also print average of the
resultant Fibonacci series."""

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