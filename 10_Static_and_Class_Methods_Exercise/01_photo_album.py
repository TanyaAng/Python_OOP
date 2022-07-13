class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.create_matrix(self.pages)

    @staticmethod
    def create_matrix(n):
        matrix = []
        for i in range(n):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // 4 + photos_count % 4
        return cls(pages)

    def free_slots(self):
        for row_idx in range(len(self.photos)):
            if len(self.photos[row_idx]) < 4:
                return row_idx

    def add_photo(self, label):
        empty_row = self.free_slots()
        if empty_row != None:
            self.photos[empty_row].append(label)
            return f"{label} photo added successfully on page {empty_row + 1} slot {len(self.photos[empty_row])}"
        return f"No more free slots"

    def display(self):
        page_separator = '-' * 11
        result = page_separator + '\n'
        is_empty_page = True
        for page in self.photos:
            for slot in page:
                if slot != '':
                    is_empty_page = False
            if is_empty_page:
                result += page_separator + '\n'
            else:
                result += ' '.join([f"[]" for photo in page if photo != '']) + '\n'
                result += page_separator + '\n'
        return result


album = PhotoAlbum(2)
# print(album.photos)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
