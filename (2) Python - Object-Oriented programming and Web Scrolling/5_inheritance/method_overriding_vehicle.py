class Vehicle:
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print(f"Turning: {self.name} to {direction}.")


class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4

    def change_gear(self, gear_name):
        print(f"{self.name} is changing gears to {gear_name}.")

    def turn(self, direction):
        print(f"{self.name} is turning to {direction}.")


if __name__ == "__main__":
    car = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    vehicle = Vehicle("Softail Delux", "Harley-Davidson", "Blue")

    car.turn("right")
    vehicle.turn("right")
