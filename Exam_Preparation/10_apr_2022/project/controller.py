class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def find_player_by_name(self, name):
        player = [p for p in self.players if p.name == name]
        if player:
            return player[0]

    def find_all_supplies_by_type(self, type):
        supplies = [s for s in self.supplies if s.__class__.__name__ == type]
        if supplies:
            return supplies

    def find_players_with_zero_stamina(self, *players):
        zero_stamina_players = [p for p in players if p.stamina == 0]
        if zero_stamina_players:
            return zero_stamina_players

    def all_player_names(self, players):
        return [p.name for p in players]

    def find_winner(self, first, second):
        second.decrease_stamina(0.5 * first.stamina)
        if second.stamina == 0:
            return first

        first.decrease_stamina(0.5 * second.stamina)
        if first.stamina == 0:
            return second
        return max(first, second)

    def add_player(self, *players):
        added_players=[]
        for player in players:
            if player not in self.players and not self.find_player_by_name(player.name):
                self.players.append(player)
                added_players.append(player)
        return f"Successfully added: {', '.join(self.all_player_names(added_players))}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name, sustenance_type):
        player = self.find_player_by_name(player_name)
        supplies = self.find_all_supplies_by_type(sustenance_type)
        if player and sustenance_type in ("Food", "Drink"):
            if not supplies:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
            if not player.need_sustenance:
                return f"{player.name} have enough stamina."
            current_supply = supplies.pop()
            self.supplies.reverse()
            self.supplies.remove(current_supply)
            self.supplies.reverse()
            player.increase_stamina(current_supply)
            return f"{player.name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name, second_player_name):
        first_player = self.find_player_by_name(first_player_name)
        second_player = self.find_player_by_name(second_player_name)
        zero_stamina_players = self.find_players_with_zero_stamina(first_player, second_player)
        if zero_stamina_players:
            result = ''
            for p in zero_stamina_players:
                result += f"Player {p.name} does not have enough stamina.\n"
            return result.strip()

        first_attacker = min(first_player, second_player)
        second_attacker = max(first_player, second_player)
        winner = self.find_winner(first_attacker, second_attacker)
        return f"Winner: {winner.name}"

    def next_day(self):
        for p in self.players:
            p.decrease_stamina(p.age * 2)
            self.sustain(p.name, 'Food')
            self.sustain(p.name, 'Drink')

    def __str__(self):
        result = ''
        for p in self.players:
            result += str(p) + '\n'
        result.strip()
        for s in self.supplies:
            result += s.details() + '\n'
        return result.strip()
