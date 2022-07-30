from extended_list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.ll = IntegerList(1, 2, 3, 4, 5)

    def test_init__with_args_of_integers(self):
        actual_result = self.ll.get_data()
        self.assertEqual([1, 2, 3, 4, 5], actual_result)

    def test_init__with_not_all_args_of_integers(self):
        ll2 = IntegerList(1, 2, '3', 4, 5)
        actual_result = ll2.get_data()
        self.assertEqual([1, 2, 4, 5], actual_result)

    def test_add__when_element_is_integer(self):
        self.ll.add(6)
        expected = [1, 2, 3, 4, 5, 6]
        actual = self.ll.get_data()
        self.assertEqual(expected, actual)

    def test_add__when_element_is_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.ll.add('6')
        self.assertIsNotNone(ex)

    def test_remove_index__when_index_is_in_range(self):
        index_to_remove = 2
        item_to_remove = self.ll.get_data()[index_to_remove]
        actual_removed_item = self.ll.remove_index(index_to_remove)
        self.assertEqual(item_to_remove, actual_removed_item)

    def test_remove_index__when_index_is_out_of_range(self):
        index_to_remove = 7
        with self.assertRaises(IndexError) as ex:
            self.ll.remove_index(index_to_remove)
        self.assertIsNotNone(ex)

    def test_get_index__when_index_is_in_range(self):
        index = 2
        expected_item = self.ll.get_data()[index]
        actual_item = self.ll.get(index)
        self.assertEqual(expected_item, actual_item)

    def test_get_index__when_index_is_out_of_range(self):
        index = 7
        with self.assertRaises(IndexError) as ex:
            self.ll.get(index)
        self.assertIsNotNone(ex)

    def test_insert__when_index_is_in_range(self):
        index = 2
        element = 100
        expected = self.ll.get_data().insert(index, element)
        actual = self.ll.insert(index, element)
        self.assertEqual(expected, actual)

    def test_insert__when_index_is_out_of_range(self):
        index = 7
        element = 100
        with self.assertRaises(IndexError) as ex:
            self.ll.insert(index, element)
        self.assertIsNotNone(ex)

    def test_insert__when_element_is_not_integer(self):
        index = 3
        element = '100'
        with self.assertRaises(ValueError) as ex:
            self.ll.insert(index, element)
        self.assertIsNotNone(ex)

    def test_get_biggest__expect_return_biggest_number(self):
        self.assertEqual(5,self.ll.get_biggest())

    def test_get_index__expect_return_index_of_element(self):
        self.assertEqual(0,self.ll.get_index(1))


if __name__ == '__main__':
    main()
