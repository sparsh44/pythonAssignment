"""Write a python program to print the Pascal’s triangle for n number of
rows given by the user using both recursive and iterative procedures
(for/while loop)."""

"""
      1 
     1 1 
    1 2 1 
   1 3 3 1 
  1 4 6  4 1 
 1 5 10 10 5 1 
1 6 15 20 15 6 1
"""
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



