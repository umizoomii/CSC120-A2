class Computer:

    # What attributes will it need? ...added all attributes from main.py
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self, name, proctype, hd_capacity, mem, operating, year, cost):
        #to initialize a computer, I want to add all of its stats here
        #self.item_id = id
        self.description = name
        self.processor_type = proctype
        self.hard_drive_capacity = hd_capacity
        self.memory = mem
        self.operating_system = operating
        self.year_made = year
        self.price = cost
        
    #returns the inventory of the computers
    def __str__(self):
        return "Description: " + self.description + ", Processor type: " + self.processor_type + ", Hard drive capacity: " + str(self.hard_drive_capacity) + ", Memory:" + str(self.memory) + ", Operating system: " + self.operating_system + ", Year made: " + str(self.year_made) + ", Price: $" + str(self.price)
    #this might need to be moved to resale shop
    
    # What methods will you need? 
        
   


    #seeing if it will print computer attrubutes
    #main
def main():
    Computer1 = Computer("2019 Macbook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    Computer2 = Computer("wowcomputer", "Microsoft", 12, 15, "idk", 2004, 5 )
    print(Computer1)
    print(Computer2)

    
if __name__ == "__main__":
    main()