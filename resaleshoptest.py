#copying the onecard code again to see what's wrong with mine

from computer import *

class ResaleShop:

    inventory: list

    #initialize class
    def __init__(self, computers):
        self.inventory = computers


    #printing things
    def __str__(self):
        return "Inventory: " + str(self.inventory)
    
    #buy computer
    def buy(self, computer: Computer):
        self.inventory.append(computer)
    

def main():
    umas_shop = ResaleShop([{"Description": "Hitech hypercode computer", "Price": 5000}, {"Description": "other computer", "Price": 2000}])
    #computerlist.buy({"Description": "yum", "Price": 2000})
    print(umas_shop)
    #computerlist.buy({"Description": Mac})
    Computer2 = Computer("wowcomputer", "Microsoft", 12, 15, "idk", 2004, 5 )
    umas_shop.buy(Computer2)
    print(umas_shop)
    
    
if __name__ == "__main__":
    main()