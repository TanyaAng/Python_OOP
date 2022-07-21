from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def find_user_by_username(self, username):
        user = [u for u in self.users_collection if u.username == username]
        if user:
            return user[0]

    def register_user(self, username: str, age: int):
        user = User(username, age)
        find_user = self.find_user_by_username(username)
        if find_user:
            raise Exception("User already exists!")
        self.users_collection.append(user)
        return f"{user.username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        if not find_user:
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if find_user != movie.owner:
            raise Exception(f"{find_user.username} is not the owner of the movie {movie.title}!")

        find_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{find_user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        find_user = self.find_user_by_username(username)
        if find_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        new_movie_attr = kwargs

        if 'title' in new_movie_attr:
            movie.title = new_movie_attr['title']
        if 'year' in new_movie_attr:
            movie.year = new_movie_attr['year']
        if 'age_restriction' in new_movie_attr:
            movie.age_restriction = new_movie_attr['age_restriction']
        return f"{find_user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        find_user = self.find_user_by_username(username)
        if find_user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        find_user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        if find_user == movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in find_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        find_user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        find_user = self.find_user_by_username(username)
        if movie not in find_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        find_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        result = '\n'.join(
            [movie.details() for movie in sorted(self.movies_collection, key=lambda m: (-m.year, m.title))])
        return result

    def __str__(self):
        if self.users_collection:
            all_usernames = ', '.join([user.username for user in self.users_collection])
        else:
            all_usernames = "No users."
        if self.movies_collection:
            all_movie_titles = ', '.join([m.title for m in self.movies_collection])
        else:
            all_movie_titles = "No movies."
        return f"All users: {all_usernames}\nAll movies: {all_movie_titles}"
