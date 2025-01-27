#FizzBuzz
for i in range(1,101):  # Loop from 1 to 100
    if i % 3 == 0 and i % 5 == 0:  # Divisible by 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif i % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:  # Not divisible by 3 or 5
        print(i)
