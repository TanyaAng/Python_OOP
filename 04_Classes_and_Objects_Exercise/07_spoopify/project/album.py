from project.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def find_song_by_name(self, name):
        searched_song = [s for s in self.songs if s.name == name]
        if searched_song:
            return searched_song[0]

    def check_if_album_is_published(self, message):
        if self.published:
            return f"{message}Album is published."
        return None

    def add_song(self, song: Song):
        is_published = self.check_if_album_is_published('Cannot add songs. ')
        if is_published:
            return is_published
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        is_published = self.check_if_album_is_published('Cannot remove songs. ')
        if is_published:
            return is_published
        searched_song = self.find_song_by_name(song_name)
        if not searched_song:
            return f"Song is not in the album."
        self.songs.remove(searched_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}\n'
        for s in self.songs:
            result += '== ' + s.get_info() + '\n'
        return result
