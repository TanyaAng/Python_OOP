class Team:
    def __init__(self, name, rating):
        self.__name=name
        self.__rating=rating
        self.__players=[]

    def find_player_by_name(self, name):
        searched_player=[p for p in self.__players if p.name==name]
        if searched_player:
            return searched_player[0]

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        searched_player=self.find_player_by_name(player_name)
        if searched_player and searched_player in self.__players:
            self.__players.remove(searched_player)
            return searched_player
        return f"Player {player_name} not found"



