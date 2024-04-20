class Bus:
    def __init__(self, route, cap):
        self.route = route
        self.cap = cap
        
    city = "Chicago"
    fare = 2.25
    
    def print(self):
        print("Bus origin:", self.city)
        print("Bus route", self.route, "has a capacity of", self.cap, "people")
        print("Bus fare:", self.fare)
    
bus1 = Bus(45, 50)
bus2 = Bus(60, 50)

bus1.print()
bus2.print()