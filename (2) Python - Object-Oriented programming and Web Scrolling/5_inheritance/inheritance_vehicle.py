class Vehicle:
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print(f"Driving: {self.manufacturer} {self.name}.")

    def turn(self, direction):
        print(f"Turning: {self.name} to {direction}.")

    def brake(self):
        print(f"Braking: {self.name}.")


class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4
        print(f"A new car has been created. Name: {self.name}.")
        print(f"It has {self.wheels} wheels.")
        print(f"The car was built in {self.year}.")

    def change_gear(self, gear_name):
        print(f"{self.name} is changing gears to {gear_name}.")


if __name__ == "__main__":
    car = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    # car.drive()
    # car.brake()
    # car.change_gear("P")
