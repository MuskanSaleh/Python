#Program to find number is prime or composite
#prime num's:2,3,5,7,11
#composite : 4,6,8,10,12,14

num = int(input("Enter a num to find whether its a prime/composite or niether prime nor composite : "))
count = 0
i = 1
while i <=num:
    if num%i == 0:
        count= count+1
    i = i+1    

if count ==2:
    print(num,"is a Prime number. ")                      
elif count >2:
    print(num,"is a Composite number.")
else:
    print(num,"is Niether prime nor composite")
