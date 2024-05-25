#class 2 
from .module1 import Car

class EletricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size = battery_size

    def display_info(self):
        return f"{self.year}{self.make}{self.model} with a {self.battery_size} - kWh battery"