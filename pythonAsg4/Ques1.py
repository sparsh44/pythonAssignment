"""Write a recursive python function to solve the problem of tower of
Hanoi with three disks."""


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