# task 1.2

class Event:
    def __init__(self, name, date, num):
        self.name = name
        self.date = date
        self.num_part = num
        
    def add_participant(self):
        self.num_part += 1
        
    def get_participant_count(self):
        print("The number of participant is", self.num_part)
        
event1 = Event("Last day of School party", "04/30", 52)
event1.get_participant_count()
event1.add_participant()
event1.get_participant_count()