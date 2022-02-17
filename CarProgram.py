import CarClass as c

def main():

    model = "civic"
    make = "honda"
    speed = 5
    
    mycar = c.Car(model, make)
    for x in range(5):
        mycar.accelerate()
        print("Speed of the car after accelerating is ", mycar.get_speed(speed))

    for y in range(5):
        mycar.brake(speed)
        print("Speed of the car after braking is ", mycar.get_speed(speed))

main()
