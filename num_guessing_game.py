import random
cnum = random.randrange(1,101)
user_input = int(input("Enter your number: "))
print("your guess number : ",user_input)
if user_input > cnum:
    print("computer number : ",cnum)
    print("Incorrect guess!!Your guess number is too high")
elif user_input < cnum:
    print("computer number : ",cnum)
    print("Incorrect guess!!Your guess number is too low")
else:
    print("computer number : ",cnum)
    print("correct guess!!Your guess num is equal")
