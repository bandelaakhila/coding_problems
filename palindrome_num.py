#palindrome of a given number
num=input()
rev=num[::-1]
if num==rev:
    print("the given number is a palindrome")
else:
    print("the given number is not a palindrome")
