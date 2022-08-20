from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    BOOK_LIMITS = 3

    def setUp(self):
        self.bookstore = Bookstore(self.BOOK_LIMITS)

    def test_attr_set_properly(self):
        self.assertEqual(self.BOOK_LIMITS, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_attr_book_limit__when_it_is_equal_to_zero(self):
        with self.assertRaises(ValueError) as ex:
            Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_attr_book_limit__when_it_is_below_to_zero(self):
        with self.assertRaises(ValueError) as ex:
            Bookstore(-5)
        self.assertEqual("Books limit of -5 is not valid", str(ex.exception))

    def test_len__when_does_not_have_books_yet__expect_zero(self):
        self.assertEqual(0, len(self.bookstore))

    def test_len__when_have_books__expect_works_properly(self):
        self.bookstore.receive_book("Harry Potter", 2)
        self.assertEqual(2, len(self.bookstore))

    def test_receive_book__when_number_exceed_book_limit(self):
        self.bookstore.receive_book("Harry Potter", 2)
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Angels and Demons", 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book__when_number_is_below_book_limit(self):
        self.bookstore.receive_book("Harry Potter", 1)
        self.assertEqual({'Harry Potter': 1}, self.bookstore.availability_in_store_by_book_titles)
        result = self.bookstore.receive_book("Harry Potter", 1)
        self.assertEqual({'Harry Potter': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"2 copies of Harry Potter are available in the bookstore.", result)

    def test_sell_book__when_book_title_not_in_book_list__expect_raise_exception(self):
        self.bookstore.receive_book("Harry Potter", 1)
        self.bookstore.receive_book("Eurocode 8", 1)
        self.bookstore.receive_book("Eurocode 2", 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Eurocode 0", 1)
        self.assertEqual(f"Book Eurocode 0 doesn't exist!", str(ex.exception))

    def test_sell_book__when_have_not_enough_copies_of_book_title__expect_raise_exception(self):
        self.bookstore.receive_book("Eurocode 2", 1)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Eurocode 2", 2)
        self.assertEqual(f"Eurocode 2 has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book__when_books_count_is_more_than_sell(self):
        self.bookstore.receive_book("Eurocode 2", 3)
        result = self.bookstore.sell_book("Eurocode 2", 2)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual({"Eurocode 2": 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 2 copies of Eurocode 2", result)

    def test_sell_book__when_books_count_is_equal_to_the_available(self):
        self.bookstore.receive_book("Eurocode 2", 2)
        result = self.bookstore.sell_book("Eurocode 2", 2)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual({"Eurocode 2": 0}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Sold 2 copies of Eurocode 2", result)

    def test_str_method(self):
        self.bookstore.receive_book("Eurocode 1", 1)
        self.bookstore.receive_book("Eurocode 2", 1)
        self.bookstore.receive_book("Eurocode 3", 1)
        self.bookstore.sell_book("Eurocode 2", 1)
        expected_result = f"Total sold books: 1\nCurrent availability: 2\n - Eurocode 1: 1 copies\n - Eurocode 2: 0 copies\n - Eurocode 3: 1 copies"
        self.assertEqual(expected_result,str(self.bookstore))


if __name__ == '__main__':
    main()
