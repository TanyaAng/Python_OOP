class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_monthly_consumption()
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = ''
        rooms_to_remove = []
        for room in self.rooms:
            room_consumption = room.room_monthly_consumption()
            if room.budget >= room_consumption:
                room.budget -= room_consumption
                result += f'{room.family_name} paid {room_consumption:.2f}$ and have {room.budget:.2f}$ left.\n'
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                rooms_to_remove.append(room)
        for room in rooms_to_remove:
            self.rooms.remove(room)
        return result.strip()

    def all_people_in_the_hotel(self):
        return sum([room.members_count for room in self.rooms])

    def status(self):
        result = f'Total population: {self.all_people_in_the_hotel()}\n'
        for room in self.rooms:
            result += str(room)
        return result.strip()
