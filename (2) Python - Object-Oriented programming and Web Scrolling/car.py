class Car:
    def __init__(self, name, manufacturer, color, year, cc):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.cc = cc

    def __repr__(self):
        return f"Car(name = {self.name}, manufacturer = {self.manufacturer}, color = {self.color}, year = {self.year}" \
               f" cc = {self.cc})"

    def start(self):
        print(f" {self.name} - Starting the engine ...")

    def brake(self):
        print(f" {self.name} - Break pressed ...")

    def drive(self):
        print(f" {self.name} - Driving the car ...")

    def turn_left(self):
        print(f" {self.name} - Turn left ...")

    def turn_right(self):
        print(f" {self.name} - Turn right ...")

    def change_gear(self, gear):
        print(f" {self.name} - Change gear to {gear} ...")


if __name__ == "__main__":
    car_1 = Car("T - 42", "Tesla", "black", "2023", "1235")
    print(car_1)
    car_1.start()
    car_1.drive()
    car_1.turn_right()
    car_1.turn_left()
    car_1.change_gear("2253")
    car_1.brake()
