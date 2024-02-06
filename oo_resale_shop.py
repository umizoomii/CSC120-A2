#importing computer data
from computer import *

#defining the class ResaleShop
class ResaleShop:

    # What attributes will it need?

    name: str #giving my shop a name!
    computers: list #inventory

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   
   #initialize inventory
    def __init__(self, name):
        self.name = name
        self.computers = []
      
    # What methods will you need?
    #print inventory, buy, update price, refurbish, sell
        
    #prints inventory with item ID: working
    def print_inventory(self):
        counter = 0 #keep track of item ID number
        for computer in self.computers:
              counter += 1
              itemID = counter
              print("Item ID: " + str(itemID) + ", " + str(computer))
        print(" ")


    #buy computer: working
    def buy(self, computer):
         print("\n Buying computer:")
         print(computer)
         self.computers.append(computer)
         print("Done! Current inventory: ")
         self.print_inventory() #print inventory to see if it added computer

    #update price: working
    def update_price(self, computer, new_price):
        if computer in self.computers:
            print("Updating price of " + str(computer.description) + "...")
            computer.price = new_price
            print("Price updated! New price: " + str(new_price))
        else:
            print("Computer not in inventory, cannot update price.")

    #refurbish computer: working
    def refurbish(self, computer, new_os = None):
        print(" ")
        if computer in self.computers: #if in inventory
            print("Refurbishing " + str(computer.description) + "...")
            if computer.year_made < 2000:
                computer.price = 0
                print("Done! New price: " + str(computer.price) + "...")
            elif computer.year_made < 2012:
                computer.price = 250
                print("Done! New price: " + str(computer.price))
            elif computer.year_made < 2018:
                computer.price = 550
                print("Done! New price: " + str(computer.price))
            else:
                computer.price = 1000
                print("Done! New price: " + str(computer.price))
        else:
            print("Error: Computer not in inventory.")
        if new_os is not None:
            computer.operating_system = new_os
            print("New operating system " + str(new_os) + " installed!")
        print(" ")


    #sell computer: working
    def sell(self, computer): #is it ok if i sell by computer name and not item ID?
        if computer in self.computers:
            print("Selling " + str(computer.description) + "...")
            self.computers.remove(computer)
            print("Computer sold! New Inventory: ")
            self.print_inventory() #print to see if computer is sold
        else:   
            print("Error: Computer not in inventory.")
    
         
    #format correctly
    def __str__(self):
        return str(self.name) + ": Printing inventory: " + str(self.computers)
    
#main function
def main():
        
        #setting up resale shop
        print(" ")
        umas_shop = ResaleShop("Uma's Resale Shop")
        print(umas_shop)
        
        #buy computers
        umas_comp = Computer("Uma's mac", "3.5 GHc 6-Core Intel Xeon E5", 20, 20, "cool Operating system", 2020, 5000)
        umas_shop.buy(umas_comp)

        cool_computer = Computer("2012 Windows computer", "Processor type", 20, 20, "some operating system", 2012, 5000)
        umas_shop.buy(cool_computer)

        #update price
        umas_shop.update_price(cool_computer, 500)
        
        #refurbish computers
        umas_shop.refurbish(umas_comp, "even cooler operating system")
        umas_shop.refurbish(cool_computer)
    
        #sell computer
        umas_shop.sell(cool_computer)
        
        #umas_shop.update_price(cool_computer, 50) (testing error message: it displays the error)
    
       
if __name__ == "__main__":
    main()