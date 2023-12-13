class Car:
    def __init__(self, speed,color):
        self.color=color
        self.speed=speed

    def start_engine(self):
        print("Vroom Vroom! The car is starting")


my_car = Car(speed=60, color="red")
your_car= Car(speed=50,color="blue")

print(my_car.color)
print(my_car.speed)



