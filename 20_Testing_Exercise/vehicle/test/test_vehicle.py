from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100.00, 200.00)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init__set_attr_fuel__expect_correct(self):
        self.assertEqual(100.00, self.vehicle.fuel)

    def test_init__set_attr_horse_power__expect_correct(self):
        self.assertEqual(200.00, self.vehicle.horse_power)

    def test_init__set_attr_capacity__expect_correct(self):
        self.assertEqual(100.00, self.vehicle.capacity)

    def test_init__set_attr_fuel_consumption__expect_correct(self):
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_is_enough__expect_fuel_decrease(self):
        self.vehicle.drive(20.00)
        self.assertEqual(75.00, self.vehicle.fuel)

    def test_drive__when_fuel_is_not_enough__expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100.00)
        self.assertIsNotNone(ex)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel__when_capacity_is_enough__expect_to_refuel(self):
        self.vehicle.drive(20.00)
        self.vehicle.refuel(15.00)
        self.assertEqual(90.00, self.vehicle.fuel)

    def test_refuel__when_capacity_is_not_enough__expect_error(self):
        self.vehicle.drive(20.00)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(50.00)
        self.assertIsNotNone(ex)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_method__expect_correct(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == '__main__':
    main()
