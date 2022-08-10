class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type):
        searched_decoration = [d for d in self.decorations if d.__class__.__name__ == decoration_type]
        if searched_decoration:
            return searched_decoration[0]
        return f"None"
