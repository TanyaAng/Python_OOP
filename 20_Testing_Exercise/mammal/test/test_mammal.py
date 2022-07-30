from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Gosho', 'donkey', 'muuu')

    def test_init__set_attr_name__expect_correct(self):
        self.assertEqual('Gosho', self.mammal.name)

    def test_init__set_attr_type__expect_correct(self):
        self.assertEqual('donkey', self.mammal.type)

    def test_init__set_attr_sound__expect_correct(self):
        self.assertEqual('muuu', self.mammal.sound)

    def test_get_kingdom__expect_to_be_animals(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound__expect_to_work_correct(self):
        self.assertEqual("Gosho makes muuu", self.mammal.make_sound())

    def test_info__expect_to_work_correct(self):
        self.assertEqual('Gosho is of type donkey', self.mammal.info())

if __name__ == '__main__':
    main()
