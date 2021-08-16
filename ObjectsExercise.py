# Object exercise

# Modelling a class from scratch: 

class Computer:
    def __init__(self, brand, year, version):
        self.brand = brand
        self.year = year
        self.version = version
    
    def printValues(self):
        print("Brand: " + self.brand + ", Year: " + str(self.year) + ", OS Version: " + self.version)

my_computer = Computer("HP", 2015, "Windows 10")
my_computer2 = Computer("Mac", 2018, "MacOS")

my_computer.printValues()
my_computer2.printValues()