input_string=input()
#part a
print(len(input_string))

#part b
reversed_string=input_string[::-1]
print(reversed_string)

#part c
sliced_String=input_string[slice(9,26)]
print(sliced_String)

#part d
new_string= input_string.replace(sliced_String," object oriented ")
print(new_string)

#part e
print(input_string.index('a'))

#part f
print(input_string.replace(" ",""))