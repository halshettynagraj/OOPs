class Hospital:
    def __init__(self,D_name, specialist, ):
        self.D_name = "Doctor_name"
        self.specialist = "specialization"
        

Govt_Hospital1 = Hospital
Hospital.D_name = "Dr.Ramkumar"
Hospital.specialist = "Heart Specialist"

print(Govt_Hospital1.D_name)

Govt_Hospital2 = Hospital
Hospital.D_name = "Dr.Rajkumar"
Hospital.specialist = "Eye Specialist"

print(Govt_Hospital2.D_name)





