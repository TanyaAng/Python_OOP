from car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car(2020, 'Peugeot', 5, 100)

    def test_init__set_attr_make__when_is_valid(self):
        self.assertEqual(2020, self.car.make)

    def test_init__set_attr_make__when_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertIsNotNone(ex)

    def test_init__set_attr_model__when_is_valid(self):
        self.assertEqual('Peugeot', self.car.model)

    def test_init__set_attr_model__when_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertIsNotNone(ex)

    def test_init__set_attr_fuel_consumption__when_is_valid(self):
        self.assertEqual(5, self.car.fuel_consumption)

    def test_init__set_attr_fuel_consumption__when_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -4
        self.assertIsNotNone(ex)

    def test_init__set_attr_fuel_capacity__when_is_valid(self):
        self.assertEqual(100, self.car.fuel_capacity)

    def test_init__set_attr_fuel_capacity__when_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -4
        self.assertIsNotNone(ex)

    def test_init__set_attr_fuel_amount__when_is_valid(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_init__set_attr_fuel_amount__when_is_not_valid(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -4
        self.assertIsNotNone(ex)

    def test_refuel__when_given_zero_or_negative_value__expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-5)
        self.assertIsNotNone(ex)
        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel__when_given_positive_value_and_total_amount_is_lower_than_capacity__expect_to_refuel(self):
        self.car.refuel(99)
        self.assertEqual(99, self.car.fuel_amount)

    def test_refuel__when_given_positive_value_and_total_amount_is_bigger_than_capacity__expect_to_refuel(self):
        self.car.refuel(101)
        self.assertEqual(100, self.car.fuel_amount)

    def test_drive__when_have_enough_fuel(self):
        self.car.fuel_amount=10
        self.car.drive(100)
        self.assertEqual(5, self.car.fuel_amount)

    def test_drive__when_does_not_have_enough_fuel(self):
        self.car.fuel_amount = 5
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertIsNotNone(ex)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))



if __name__ == '__main__':
    main()
