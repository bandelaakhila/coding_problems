#friendly pair:
'''
step 1 : take the two input num
step 2 : find the factors of the numbers
step 3 : calculate the sum of the factors
step 4 : if the number and sum of the factors of the number is equal then it is said to be friendly pair
'''
n1=int(input())
n2=int(input())
s1=0
s2=0
for i in range(1,n1):
    if (n1%i==0):
        s1+=i
for j in range(1,n2):
    if (n2%j==0):
        s2+=j
if n1/n2==s1/s2:
    print("friendly pair")
else:
    print("not friendly pair")
