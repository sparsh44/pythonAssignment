"""Write a Python program to create a list of tuples with the first element as the
number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""
list1=[]
n=int(input("ENTER NUMBER OF ELEMENTS YOU WANT : "))
for i in range(0,n):
   a=int(input())
   list1.append(a)
list2=[]
for x in list1:
   list2.append((x,x**2))
print(list2)