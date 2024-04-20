# task 1.1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def print_owner(self):
        print("The owner is", self.owner)
        
    def update_owner(self, new_owner):
        self.owner = new_owner
        
vehicle1 = Vehicle(10, "suv", "Kris")
vehicle1.print_owner()

vehicle1.update_owner("Kelly")
vehicle1.print_owner()



    
    