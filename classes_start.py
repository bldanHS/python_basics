#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Building():
    def __init__(self, style):
        self.style = style

    def buildingTime(self, hours):
        self.hours = hours
        
    
class Townhouse(Building):
    def __init__(self, style):
        super().__init__("Townhouse")
        self.windows = 100
        self.height = 50
        self.style = style

    def buildingTime(self, hours):
        super().buildingTime(hours)
        print("This house takes ", str(self.hours), "hours to be built")



class Bungalow(Building):
    def __init__(self, style, hasgarden):
        super().__init__("Bungalow")
        self.windows = 3
        self.height = 4
        if (hasgarden):
            self.parcel = 200
        else:
            self.parcel = 50
        self.style = style


    def buildingTime(self, hours):
        super().buildingTime(hours)
        print("This house takes ", str(self.hours), "hours to be built")



bung1 = Bungalow("low", False)
townh1 = Townhouse("high")

print("Bungalow house: ")
print(bung1.height)
print(bung1.windows)
print(bung1.buildingTime(99))

print("Townhouse: ")
print(townh1.height)

print(townh1.windows)
print(townh1.buildingTime(667))

