import random

class Insect:
    def __init__(self,w, l):
        self.wings = w
        self.legs = l
        self.length = 0

    def lengthofflight(self):   
        self.length = random.randint(1, 10)
        
    def get_flight(self):
        return self.length
