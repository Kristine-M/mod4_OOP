class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        
    def save_from_file(self, filename):
        
        with open(filename, 'r') as file:
           
            for line in file:
                self.name, self.floors = line.strip().split(',')
                
    def print(self):
        print(self.name)
        print(self.floors)
                
    def load_into_file(self, filename):
        
        file = open(filename, 'w')
        file.write(self.name)
        file.write("\n")
        file.write(str(self.floors))
        
        file.close()
            
building1 = Building("N/A", 0)

building1.save_from_file("building_source.txt")
building1.print()
building1.load_into_file("building_output.txt")