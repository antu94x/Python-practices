char=input("Enter an alphabet =")
a=["a","e","i","o","u"]
if char in a:
    print(char,"is a vowel")
elif char.isalpha():
    print(char,"is a vowel")
else:
    print(char,"is a consonant")