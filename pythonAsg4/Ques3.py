"""Input two integer values from user, calculate and print the quotient
and reminder obtained from the two values,
a) Check whether it(function/values) is callable or not.
b) Check whether all the values are non zeros or not.
c) Add values (4, 5, 6) to the result and filter out the values which
are greater than 4.
d) Convert the above result into set datatype.
e) Make that set immutable.
f) Evaluate the maximum value from set and find out its hash
value."""

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