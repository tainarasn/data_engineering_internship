from modules.module1 import Car
from modules.module2 import EletricCar

def main():
    my_car = Car("Toyota", "Corolla", 2020)
    print(my_car.display_info())

    my_eletric_car = EletricCar("Tesla", "Model S",2021,100)
    print(my_eletric_car.display_info())

if __name__== "__main__":
    main()