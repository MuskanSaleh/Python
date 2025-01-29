#program to convert decimal to binary,octal and hexadecimal

user = int(input("Enter a number :"))
print("Decimal Number is :",user)
binaryy = bin(user)
octal = oct(user)
hexa=hex(user)
print("Binary of",user,"is :",binaryy)
print("Octal of",user,"is :",octal)
print("Hexadecimal of",user,"is :",hexa)
