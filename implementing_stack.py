##Implement a stack  using a list datatype
#stack is a linear datastructure
#it stores tems in LIFO(last-in/first-out) or FILO(first-in/last-out)manner
#stack operations:push,pop,peek,display

l = []
while True:
    opr = int(input("""
        select the number to perform operations on stack:
         1.Push Elements
         2.Pop Elements
         3.Peek Elements
         4.Display Elements
         5. Exit
      
      """))
    if opr == 1:
        inp = input("Enter the value to add : ")
        l.append(inp)
        print(l)
    elif opr == 2:
        if len(l) == 0:
            print("Empty stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif opr == 3:
        if len(l) == 0:
            print("Empty stack")
        else:
            print("last stack value : ",l[-1])
    elif opr == 4:
        if len(l) == 0:
            print("Empty stack")
        else:
            print("Display stack : ",l)
    elif opr == 5:
        print("Program exited successfully!!")
        break;

