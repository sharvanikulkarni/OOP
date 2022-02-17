#from statistics import mode
import CellPhoneClass as cp

def main():
    
    phone = cp.CellPhone("apple", "iphone", 300)
    print("The name of the manufacturer is: ", phone.get_manufact())
    print("The name of the manufacturer is: ", phone.get_model())
    print("The name of the manufacturer is: ", phone.get_retial_price())
    
main()