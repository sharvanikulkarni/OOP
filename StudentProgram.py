import StudentClass as s

def main():
    my_student = s.Student(1234, "sharvani", "02/02/1993", "S")
    #my_student.Calc_Age()
    
    print(my_student.Calc_Age())
    print(my_student.Get_Registration_Details())
main()

