# tests/test_module1.py

import unittest
from src.modules.module1 import Car


class TestCar(unittest.TestCase):
    def test_display_info(self):
        car = Car("Toyota", "Corolla",2020)
        self.assertEqual(car.display_info(),'2020 Toyota Corolla')
        
if __name__ == "__main__":
    unittest.main()