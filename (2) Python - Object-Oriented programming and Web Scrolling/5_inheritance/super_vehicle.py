class Vehicle:
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Car(Vehicle):
    def __init__(self, name, manufacturer, color, year):
        print("Creating a car..!")
        super().__init__(name, manufacturer, color)
        self.year = year
        self.wheels = 4


if __name__ == "__main__":
    car = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
    print(car.name, car.manufacturer, car.color, car.year, car.wheels)
