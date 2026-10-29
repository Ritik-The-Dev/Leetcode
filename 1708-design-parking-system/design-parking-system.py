class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.small = small     
        self.medium = medium        
        self.big = big   

    def addCar(self, carType: int) -> bool:
        
        match carType:
            case 1 :
                if self.big > 0:
                    self.big -= 1
                    return True
                else:
                    return False
            case 2:
                if self.medium > 0:
                    self.medium -= 1
                    return True
                else:
                    return False
            case 3:
                if self.small > 0:
                    self.small -= 1
                    return True
                else:
                    return False
            case _:
                return "Invalid Size"



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)