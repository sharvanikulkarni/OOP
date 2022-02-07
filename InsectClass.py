import random

class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.length = 0

    def lengthofflight(self):   
        self.length = random.randint(1,10)
