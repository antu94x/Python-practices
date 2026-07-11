char=input("Enter an alphabet =")
a=["a","e","i","o","u"]
lower_char=char.lower()
if lower_char in a:
    print(char,"is a vowel")
elif lower_char.isalpha():
    print(char,"is consonant")
else:
    print(char,"is not an alphabet character. Pls enter an alphabet...")