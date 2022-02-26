"""Barbie and George are the two friends. On Saturday, they decided to
travel to a fair where they discovered a fun game that put their
friendship to the test. The test required George to utter a word and
Barbie to create a new meaningful word using the exact same letters
as George. If Barbie fails to form a word then their friendship is a fake.

Can you assist the shopkeeper by writing a piece of code for him to
use so that the test runs smoothly?"""

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