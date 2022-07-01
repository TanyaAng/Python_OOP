from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id, new_username, library: Library):
        searched_user = [user for user in library.user_records if user.user_id == user_id]
        if not searched_user:
            return f"There is no user with id = {user_id}!"
        current_user = searched_user[0]
        if new_username == current_user.username:
            return f"Please check again the provided username - it should be different than the username used so far!"
        previous_username = current_user.username
        current_user.username = new_username
        if previous_username in library.rented_books:
            library.rented_books[new_username] = library.rented_books.pop(previous_username)
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
