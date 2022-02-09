"""Given the sets below, write python statement to:
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
a. Create a new set of all elements that are in Set1 and Set2 but not both.
b. Create a new set of all elements that are in only one of the three sets Set1,
Set2 and Set3.
c. Create a new set of elements that are exactly two of the sets Set1, Set2
and Set3.
d. Create a new set of all integers in the range 1 to 10 that are not in Set1.
e. Create a new set of all integers in the range 1 to 10 that are not in Set1,
Set2 and Set3."""

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
