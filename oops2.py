class Vehicle:
    def __init__(self,M_name, M_year, M_engine_type):
        self.name = M_name
        self.year = M_year
        self.enginetype = M_engine_type


Tata = Vehicle
Tata.name = "Nexon"
Tata.year = 2020
Tata.enginetype = "Petrol"

print(Vehicle.year)

Hundai = Vehicle
Hundai.name = "Creata"
Hundai.year = 2022
Hundai.enginetype = "Diesel"

print(Vehicle.name)
        