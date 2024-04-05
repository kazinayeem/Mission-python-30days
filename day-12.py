# day 12

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('Audi', 'A4', 2020)
print(my_car.get_descriptive_name())
# Output: 2020 Audi A4

print(my_car.read_odometer())
# Output: This car has 0 miles on it.

my_car.update_odometer(100)
print(my_car.read_odometer())
# Output: This car has 100 miles on it.

my_car.increment_odometer(50)
print(my_car.read_odometer())


# Output: This car has 150 miles on it.
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


my_electric_car = ElectricCar('Tesla', 'Model S', 2022, 75)

print(my_electric_car.get_descriptive_name())
# Output: 2022 Tesla Model S

print(my_electric_car.describe_battery())
# Output: This car has a 75-kWh battery.
