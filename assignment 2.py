
#Write a program to find the factorial of user input number.
'''======================================================
a=int(input("Enter the number: "))
factoral=1
if a==0:
    print("1 is a factoial")
else:
    for i in range(1,a+1):
        factoral=factoral*i
    print("The factorial is",factoral)
========================================================== '''
#Given an integer n, print all integers less then or equal to n
'''=============================================================
a=int(input("Enter the number: "))
j=1
while j <=a :
    print(j,end=' ')
    j+=1
================================================================='''
#Given an integer, print the sum of all even integers less then or equal to n
'''==============================================================
sum=0
a=int(input("Enter the number: "))
for i in range(1,a+1):
    if(i%2==0):
        sum=sum+i
print(sum)
==================================================================='''
#Given n, print the sum of all integers less then or equal to n which are divisible by 3 or 5
'''==========================================================================================
a=int(input("Enter the value: "))

a=int(input("Enter the number: "))
sum=0
for i in range(1,a+1):
    if((i%3==0) | (i%5==0)):
        sum=sum+i
print(sum)
================================================================================================='''