from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    SHOP_NAME = 'Topcho'

    def setUp(self) -> None:
        self.petshop = PetShop(self.SHOP_NAME)

    def test_attr_set_properly(self):
        self.assertEqual(self.SHOP_NAME, self.petshop.name)
        self.assertEqual({}, self.petshop.food)
        self.assertEqual([], self.petshop.pets)

    def test_add_food__when_it_is_not_valid(self):
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food('meat', -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food__when_successfully(self):
        self.petshop.add_food('meat', 5)
        result = self.petshop.add_food('meat', 2)
        self.assertEqual({'meat': 7}, self.petshop.food)
        self.assertEqual("Successfully added 2.00 grams of meat.", result)

    def test_add_pet__when_it_is_not_valid(self):
        self.petshop.add_pet('Pesho')
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet('Pesho')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet__when_it_is_added_successfully(self):
        result = self.petshop.add_pet('Pesho')
        self.assertEqual(['Pesho'], self.petshop.pets)
        self.assertEqual("Successfully added Pesho.", result)

    def test_feed_pet__when_pet_not_in_pets(self):
        self.petshop.add_pet("Pesho")
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet("fish", "Gosho")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet__when_pet_in_pets_but_food_not_in_foods(self):
        self.petshop.add_pet("Pesho")
        self.petshop.add_food('fish', 10)
        result = self.petshop.feed_pet("meat", "Pesho")
        self.assertEqual('You do not have meat', result)

    def test_feed_pet__when_food_quantity_is_not_enough(self):
        self.petshop.add_pet("Pesho")
        self.petshop.add_food('fish', 10)
        result = self.petshop.feed_pet("fish", "Pesho")
        self.assertEqual({'fish':1010}, self.petshop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet__when_pet_is_successfully_fed(self):
        self.petshop.add_pet("Pesho")
        self.petshop.add_food('fish', 110)
        result = self.petshop.feed_pet("fish", "Pesho")
        self.assertEqual({'fish':10}, self.petshop.food)
        self.assertEqual("Pesho was successfully fed", result)

    def test_repr__when_have_pets_in_repository(self):
        self.petshop.add_pet("Pesho")
        self.petshop.add_pet("Gosho")
        result=f'Shop {self.SHOP_NAME}:\n' \
               f'Pets: Pesho, Gosho'
        self.assertEqual(result, self.petshop.__repr__())

    def test_repr__when_have_no_pets_in_repository(self):
        result=f'Shop {self.SHOP_NAME}:\n' \
               f'Pets: '
        self.assertEqual(result, self.petshop.__repr__())


if __name__ == '__main__':
    main()
