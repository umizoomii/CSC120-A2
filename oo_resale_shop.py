#importing computer data
from computer import *

class ResaleShop:

    # What attributes will it need?

    name: str
    computers: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   #initialize inventory
    def __init__(self, name):
        self.name = name
        self.computers = []
       # counter = 0 working on setting up ID system
        #for computer in computers:
        #     counter += 1
        #     self.itemID = computers[counter]
        #     print("Computer " + str(self.itemID) + str(computer))
   
    # What methods will you need?
    
    #print inventory, buy, refurbish, sell
        
    #prints inventory and assigns item id
    def print_inventory(self):
        counter = 0
        for computer in self.computers:
              counter += 1
              print("Item ID: " + str(counter) + ", " + str(computer))


    #buy computer
    def buy(self, computer):
         print("Buying computer:")
         print(computer)
         self.computers.append(computer)
         print("Done! Current inventory: ")
         self.print_inventory() #print inventory to see if it added computer

    
    #refurbish computer: (some errors here)
    #def refurbish(self, computer):
    #    if int(self.computer["Year"]) < 2000:
    #        int(self.computer["Price"]) == 0

    #sell computer: currently not working
    def sell(self, itemID):
        if self.computers[itemID] in self.computers:
            del self.computers[itemID]
            print("Item " + str(itemID) + " sold! New Inventory: ")
            self.print_inventory() #print to see if computer is sold
        else:   
            print("Item ID does not exist.")
    
         
    #print inventory
    def __str__(self):
        return str(self.name) + ": Printing inventory: " + str(self.computers)
    #main function

def main():
        
        #setting up resale shop
        print(" ")
        umas_shop = ResaleShop("Uma's Resale Shop")
        print(umas_shop)
        
        
        #buy computers: seems to be working
        umas_comp = Computer("Uma's mac", "idk", 20, 20, "cool Operating system", 1900, 5000)
        umas_shop.buy(umas_comp)

        cool_computer = Computer("Windows", "Processor type", 20, 20, "Operating", 1900, 5000)
        umas_shop.buy(cool_computer)
        
        #refurbish computer:
        #oldcomputer = Computer("ancient technology", "Processor type", 20, 20, "Operating", 1800, 5000)
        #umas_shop.refurbish(oldcomputer)
        #print(oldcomputer)
       
        #sell computer
        print("Selling computer...")
        umas_shop.sell(1)
        #print(umas_shop)
        #print("Done!")
       
if __name__ == "__main__":
    main()