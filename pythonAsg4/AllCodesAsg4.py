#QUES1

# Recursive Python function to solve the tower of hanoi
 
def TowerOfHanoi(n , source, destination, helper):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, helper, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, helper, destination, source)
         
# Driver code
n = 3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods

#QUES 2

n=int(input("Enter n: "))
print("Using Loops")
def printPascal(n:int):
 
    arr = [[0 for x in range(n)]
              for y in range(n)]
 
    # Iterate through every line
    for line in range (0, n):
        print(" "*(n-line),end = " ")
        # Every line has number of
        # integers equal to line number
        for i in range (0, line + 1):
 
            # First and last values
            # in every row are 1
            if(i == 0 or i == line):
                arr[line][i] = 1
                print(arr[line][i], end = " ")
 
            # Other values are sum of values
            # just above and left of above
            else:
                arr[line][i] = (arr[line - 1][i - 1] +arr[line - 1][i])
                print(arr[line][i], end = " ")            
        print("\n", end = "")
printPascal(n)


print("Using Recursion")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)


#QUES 3

a, b = map(int,input("Enter 2 numbers: ").split())
Quotient = a // b
Remainder = a % b

#Part a
print("Part a")
print("Using Callable function")
print(callable(Quotient))
print(callable(Remainder))

#Part b
print("Part b")

if (Quotient == 0):
    print("The quotient is zero")
if (Remainder == 0):
    print("The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("All the values are non zero")

#Part c
print("Part c")

partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#Part d
print("Part d")

res = set(result)
print("Set:",res)

#Part e
print("Part e")

immutableSet = frozenset(res) #frozen Set is used to make the set immutable
print("Immutable set is :",immutableSet)

#Part f
print("Part f")

print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

#QUES 4

class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __del__(self):
        print("Object destroyed")

obj=Student("Sparsh",21103084)

print(obj.name)
print(obj.roll)
del obj

#QUES 5

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
        

# storing employee details

e1=Employee("Mehak",40000)
e2=Employee("Ashok",50000)
e3=Employee("Viren",60000)



#Part a
print("Part a")
e1.salary=70000
print(f"The updated salary of {e1.name} is {e1.salary} ")
#part b
print("Part b")
del e3
print("Record of Viren is deleted")


#QUES 6

def anagrams(s):
 if s == "":
    return [s]
 else:
    ans = []
 for w in anagrams(s[1:]):
    for pos in range(len(w)+1):
        ans.append(w[:pos]+s[0]+w[pos:])
 return ans

s=input("George Says : ")
s2=input("Barbie Says : ")

li=anagrams(s)
if s2 in li:
   print("friendship is a nice")
else:
   print("friendship is a fake")