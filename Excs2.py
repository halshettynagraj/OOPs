class student:
    def res(self):
        self.marks = int(input("enter marks : "))
        if self.marks < 40 :
            return "Fail"
        else:
            return "Pass"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


rollnum1 = student ("ram", 85)

print("student name is : ", rollnum1.name)
result = rollnum1.res()
print(result)


    
