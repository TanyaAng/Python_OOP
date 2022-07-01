from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}  # {author: [books]}
        self.rented_books = {}  # {username: {book_names: days_to_return}}

    def find_user_by_username(self, name):
        searched_user = [user for user in self.user_records if user.name == name]
        if searched_user:
            return searched_user[0]

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name not in self.books_available.get(author):
            days_to_return = 0
            for value_dict in self.rented_books.values():
                for key, value in value_dict.items():
                    if key == book_name:
                        days_to_return = value
                        break
            return f'The book "{book_name}" is already rented and will be available in {days_to_return} days!'

        if book_name in self.books_available.get(author):
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = {book_name: days_to_return}
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        if user in self.user_records:
            if book_name not in user.books:
                return f"{user.username} doesn't have this book in his/her records!"
            user.books.remove(book_name)
            username = user.username
            self.books_available[author].append(book_name)
            del self.rented_books[username][book_name]
