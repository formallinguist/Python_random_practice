#3.11 super anagram.
def super_anagram(b,c):
  if b[-1] == c[-1]:
    if sorted(b) == sorted(c):
        return "super Anagram!"
  else:
    return "What?"

a = input("Enter two words:").split(" ")
b = a[0]
c = a[1]

print(super_anagram (b,c))