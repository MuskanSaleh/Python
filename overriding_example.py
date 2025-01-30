#Overriding...same name same arguments..impplrmrnted with inheritance also..
#mostly used for memory reducing processes

class A:
    def showdata(self):
        print("I'm in A")
class B(A):
    def showdata(self):
        #super().showdata()#to call class A function
        print("I'm in B")

obj =B()
obj.showdata()
