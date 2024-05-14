class Vehicle:
    def __init__(self, name, max_speed, mileage):
         self.name = name
         self.max_speed = max_speed
         self.mileage = mileage
         
    def summary(self):
        print("The " + self.name + " goes a maximum speed of " + str(self.max_speed) + " and has " + self.mileage + " mileage.")
        
class Bus(Vehicle):
    def __init__(self, company, school, name, max_speed, mileage):
        self.company = company
        self.school = school
        super().__init__(name, max_speed, mileage)
        
    def what_school(self):
        print(self.name + " goes to " + self.school_name)

    def what_company(self):
        print(self.name + " belongs to " + self.company)

bus1 = Bus("ford", 130, "1400 miles", "the big company", "metuchen middle school")

bus1.summary()        