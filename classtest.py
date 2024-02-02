
#tested on a separate document to fix error, using onecard example (program was not identifying class "computer")
class Computer:
    ogname = str
    ogprice = float

    def __init__(self, name, price):
        self.ogname = name
        self.ogprice = price

    def __str__(self):
        return self.ogname + " is " + str(self.ogprice)

def main():
    myComputer = Computer("Mac", 500)
    print(myComputer)

if __name__ == "__main__":
    main()