#abudant number
'''
a num that is smaller than the sum of its factors except the number itself is known as abudant num
'''
num=int(input())
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum>num):
    print("abudant number")
else:
    print("not an abudant number")
