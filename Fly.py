import InsectClass as i

def main():
    my_insect = i.Insect(2,4)
    print("initial=",my_insect.get_flight())
    my_insect.lengthofflight()
    
    print("Number of miles the insect can fly: ", my_insect.get_flight())
    
main()