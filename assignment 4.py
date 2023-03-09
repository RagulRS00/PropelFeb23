#1
'''==================================================
a=[]
odd=[]
even=[]
def sort_odd_even():
    b=int(input("Enter the number"))
    for i in range (b):
        c=int(input("Enter the number"))
        a.append(c)
    for i in a:
        if i%2==0:
            even.append(i)
            even.sort()
        else:
            odd.append(i)
            odd.sort()
    print(odd+even)
sort_odd_even()
========================================================'''
#2
'''======================================================
list=[12,24,35,24,88,120,55,24]
newList=[i for i in list if i!=24]
print(newList)
=========================================================='''
