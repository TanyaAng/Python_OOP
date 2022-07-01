from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def find_player_by_name(self, name):
        searched_player = [p for p in self.players if p.name == name]
        if searched_player:
            return searched_player[0]
        return None

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != Player.initial_guild_status:
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        searched_player=self.find_player_by_name(player_name)
        if not searched_player:
            return f"Player {player_name} is not in the guild."
        self.players.remove(searched_player)
        searched_player.guild=Player.initial_guild_status
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result=f'Guild: {self.name}\n'
        for p in self.players:
            result+=p.player_info()
        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
