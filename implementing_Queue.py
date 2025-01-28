#Implementing queue
#Queue is also a linear data structure
#Stores items in FIFO(First In First Out)manner
#Queue operations:Enqueue,Dequeue,Front,Rear

l = []
while True:
    c = int(input(""""
                  1.Push/Enqueue Elements
                  2.Pop/Dequeue First Elements
                  3.Front Elements
                  4.Rear/Last Elements
                  5.Display Queue
                  6.Exit

                  """))
    if c == 1:
        inp = input("Enter the value to add : ")
        l.append(inp)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Empty Queue")
        else:
            del l[0]
            print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Front value : ",l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Last Queue Element : ",l[-1])
    elif c == 5:
        if len(l) == 0:
            print("Empty Queue")
        else:
            print("Display Queue : ",l)
    elif c == 6:
        print("Program exited successfully!!")
        break;
    else:
        print("Invalid choice")
