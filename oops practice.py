class vehicle:
    def __init__(self, name, maxspeed, milage):
        self.name = name
        self.maxspeed = maxspeed
        self.milage = milage
    

class Bus(vehicle):
    pass

School_Bus = Bus("volvo", 200, 35)
print("Vehicle name", School_Bus.name, "Maxspeed", School_Bus.maxspeed, "milage", School_Bus.milage)






