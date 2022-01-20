num1=int(input())
num2=int(input())
num3=int(input())

list1=[num1,num2,num3]
max=num1
i=1
while i<len(list1):
    if(max<list1[i]) :
        max=list1[i]
        i=i+1
    else:
        i=i+1
print(max)