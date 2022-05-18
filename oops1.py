# class Vehicle:
#     def GetDetails(self, color, model, Year):
#         Dict1 = {"color" : "Red", "Model" : "Maruthi", "Year" : 2020}
#         Dict = {"color" : "black", "Model" : "palsur", "Year" : 2022}

class student:
    def __init__(self, name, id, std):
        self.id = id
        self.name = name
        self.std = std

A = student
A.id = 1
A.name = "ram"
A.std = "10th"

print ("student id is", A.id, "Student name is", A.name, "and he is a", A.std, "stanard")

B = student
B.id = 2
B.name = "sham"
B.std = "9th"

print(B.id, B.name, B.std)
