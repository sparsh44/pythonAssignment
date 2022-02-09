"""Write a Python program to create a list of tuples with the first element as the
number and Second element as the square of the number.
E.g. list = [3, 9, 10]
Output: [(3, 9), (9, 81), (10, 100)]"""
list1=[3,9,10]
list2=[]
for i in list1:
   list2.append((i,i**2))
print(list2)