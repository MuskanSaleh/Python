#Bike Rental System

class bikeshop:
    #constructor for stock
    def __init__(self,stock):
        self.stock=stock
    #method for display total available bikes
    def displayBike(self):
        print("Total Bikes : ",self.stock) 
    #method for rentbike  
    def RentForBike(self,q):

        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q>self.stock:
            print("Enter the value(less then stock)")
        else:
            self.stock = self.stock-q
            print("Total price : ",q*100)
            print("Total Available stock : ",self.stock)

while True:
    obj = bikeshop(100)
    ui = int(input("""
                  1.Display available stocks
                  2.Request a bike for rent(100 Rs -> 1qty)
                  3.Exit """))
    if ui==1:
        obj.displayBike()
    elif ui==2:
        n=int(input("Enter the qty u would like to rent : "))
        obj.RentForBike(n)
    else:
        break
