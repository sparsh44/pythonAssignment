"""
ABCDEFGHIJK
 ABCDEFGHI
  ABCDEFG
   ABCDE
    ABC
     A"""

x=0
for j in range(0,6):
    print(" "*j,end="")
    i=65
    for i in range(65,76) :
        if i==76-x:
            break
        print(chr(i),end="")   # using ASCII values and typecasting
    x=x+2
    print(" ")