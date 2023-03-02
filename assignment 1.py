'''===========================================================
#1WRITE A PROGRAM TO CHECK WETHER THE INPUT IS ODD OR EVEV
x=int(input("enter the value :"))
if (x % 2 ==0):
    print("this is EVEN")
else:
 print("This is odd")
==============================================================='''
#2
'''=============================================================
x=int(input("enter the value :"))
if (x % x ==0 ):
    print(("this is a prime number"))
else:
    print(("its not prime numbere"))
================================================================='''
#QUESTION NUMBER :3
'''==============================================================
ageOfPerson=int(input("Enter your age :"))
if (ageOfPerson >= 18):
    print("You are eligiable for voting")
else:
    print("you are not eligiable for voting")
================================================================='''
#QUESTION NUMBER 4
'''==============================================================
num=int(input("Enter a number:"))
if(num %7==0 & num%8==0):
    print("Its divisible by 7 or 8")
else:
    print("not divisible by 7 or 8")
=================================================================='''
#QUESTION NUMBER 5
'''===============================================================
usedUnit=int(input("Enter the amount of electricity you used:"))
if usedUnit <=100:
    print("no charge")
elif usedUnit <201:
    print("5 is your charge")

else:
    extraUse=usedUnit-200
    print("extra Usage ",extraUse)
    totalCost=(500+(extraUse*10))

    print(totalCost,"is your charge amount")
==================================================================='''