from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Pesho', 3, 15.00, 5.00)

    def test_init__set_attr_username__expect_work_correct(self):
        self.assertEqual('Pesho', self.hero.username)

    def test_init__set_attr_level__expect_work_correct(self):
        self.assertEqual(3, self.hero.level)

    def test_init__set_attr_health__expect_work_correct(self):
        self.assertEqual(15.00, self.hero.health)

    def test_init__set_attr_damage__expect_work_correct(self):
        self.assertEqual(5.00, self.hero.damage)

    def test_battle__when_username_is_the_same_as_the_first_hero__expect_error(self):
        enemy_hero = Hero('Pesho', 5, 20.00, 10.00)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertIsNotNone(ex)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle__when_health_of_hero_is_less_than_0__expect_error(self):
        enemy_hero = Hero('Stamat', 5, 20.00, 10.00)
        self.hero.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertIsNotNone(ex)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle__when_health_of_enemy_is_less_than_0__expect_error(self):
        enemy_hero = Hero('Stamat', 5, -20.00, 10.00)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertIsNotNone(ex)
        self.assertEqual("You cannot fight Stamat. He needs to rest", str(ex.exception))

    def test_battle__when_health_of_hero_and_enemy_become_less_than_zero__expect_draw(self):
        hero = Hero('Pesho', 3, 10.00, 10.00)
        enemy_hero = Hero('Stamat', 5, 20.00, 10.00)
        actual_result = hero.battle(enemy_hero)
        self.assertEqual(-40.0, hero.health)  # 10-5*10=-40
        self.assertEqual(-10.0, enemy_hero.health)  # 20-30 = -10
        self.assertEqual('Draw', actual_result)

    def test_battle__when_hero_wins__expect_message(self):
        hero = Hero('Pesho', 3, 100.00, 10.00)
        enemy_hero = Hero('Stamat', 5, 20.00, 10.00)
        actual_result = hero.battle(enemy_hero)
        self.assertEqual(55.0, hero.health)
        self.assertEqual(4, hero.level)
        self.assertEqual(15, hero.damage)
        self.assertEqual(-10.0, enemy_hero.health)
        self.assertEqual('You win', actual_result)

    def test_battle__when_hero_lose__expect_message(self):
        hero = Hero('Pesho', 3, 10.00, 10.00)
        enemy_hero = Hero('Stamat', 5, 200.00, 10.00)
        actual_result = hero.battle(enemy_hero)
        self.assertEqual(6, enemy_hero.level)
        self.assertEqual(175.0, enemy_hero.health)
        self.assertEqual(15, enemy_hero.damage)
        self.assertEqual(-40.0, hero.health)
        self.assertEqual('You lose', actual_result)

    def test_str__expect_to_work_correct(self):
        result=f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()
