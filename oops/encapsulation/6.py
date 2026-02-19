class Car:
    def __init__(self):
        self.__speed = 0
        self.__max_speed = 180

    def increase_speed(self, value):
        if value < 0:
            print("Invalid value!")
            return

        if self.__speed + value > self.__max_speed:
            self.__speed = self.__max_speed
            print("Reached maximum speed limit!")
        else:
            self.__speed += value
            print(f"Speed increased by {value} km/h")

    def decrease_speed(self, value):
        if value < 0:
            print("Invalid value!")
            return

        if self.__speed - value < 0:
            self.__speed = 0
            print("Car has stopped.")
        else:
            self.__speed -= value
            print(f"Speed decreased by {value} km/h")

    def display_speed(self):
        print("Current Speed:", self.__speed, "km/h")

car = Car()

car.increase_speed(50)
car.display_speed()

car.increase_speed(200)
car.display_speed()

car.decrease_speed(30)
car.display_speed()

car.decrease_speed(100)
car.display_speed()
