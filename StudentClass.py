
from sys import dont_write_bytecode
from unicodedata import name
from datetime import date

class Student:
    def __init__(self, studentid, studentname, Bdate, classification):
        self.__Studentid = studentid
        self.__Studentname = studentname
        self.__Bdate = Bdate
        self.__classification = classification

    def Calc_Age(self):
        today = date.today()
        born = self.__Bdate.split("/")
        bornyear = int(born[2])
        age = today.year - bornyear
        return age

    def Get_Registration_Details(self):
        if self.__classification == "F":
            return "Freshmen - 11/10 thru 11/12"
        elif self.__classification == "S":
            return "Sophomores - 11/7 thru 11/9"
        elif self.__classification == "Jr":
            return "Juniors - 11/4 thru 11/6"
        elif self.__classification == "Sr":
            return "Seniors - 11/1 thru 11/3"
        else:
            return "This classification does not exist"


            

