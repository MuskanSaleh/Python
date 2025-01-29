#program to print fibonacci sequence...sum of pre consecutive numbers
#0,1,1,2,3,5,8...
inp=int(input("Enter the num till u want the series :"))
a = 0
b = 1
c = 0
i = 1
print(a)
print(b)
while i < inp:
    c=a+b
    a = b
    b = c
    i = i+1
    print(c)

print("The fibonacci series for the given no 10 is : ",c)
