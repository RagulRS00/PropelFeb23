# Assignments:3

# write a function to check wether input string is palindrome

'''=========================================================================

a=input("Enter the element :")
def checkPalindrome(a):
    if a==a[::-1]:
        print(a,"is a Palindrome")
    else:
        print(a,'is not a palindrome')

checkPalindrome(a)
=================================================================================='''
# write a function to find the factorial of a number.
'''================================================================================
a=int(input('enter the value :'))
def factorial(a):
    if a==0:
        return 1
    else:
        return a * factorial(a-1)
print('vale is:',factorial(a))
========================================================================================'''
# write a function to find the fibonacci series of the number
'''======================================================================================
def fib(n):
    L=[0]#intialise first element with 0
    a,b=0,1#a=0 b=1
    for i in range(n):
        a,b=b,a+b #a=b b=a+b
        L.append(a)
    return L
print(fib(int(input('Enter the number :'))))
==========================================================================================='''