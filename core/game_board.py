from random import choice, randint, shuffle
from typing import List

from models.player import Player, PlayerConduct
from models.property import Property
from models.simulation_result import SimulationResult
from settings import MAXIMUM_AMOUNT_OF_MATCHES


class GameBoard:
    properties = List[Property]
    default_players = [Player.create_player(list(PlayerConduct)[index]) for index in range(len(PlayerConduct))]
    players = List[Player]
    eliminated_players = []
    result = List[tuple]
    timeout = 0
    winner = None

    def __init__(self):
        self.properties = Property.create_game_board_properties()
        self.shuffle_players()

    def shuffle_players(self):
        default_players = self.default_players
        shuffle(default_players)
        self.players = default_players

    def start_game(self) -> SimulationResult:
        match_counter = 1
        while match_counter <= MAXIMUM_AMOUNT_OF_MATCHES:
            for index_player in range(0, len(self.players)):
                player = self.players[index_player]
                if player in self.eliminated_players:
                    continue

                new_position = self.get_new_player_position(player.current_position)
                player.current_position = new_position
                player.rounds += 1

                property = self.properties[new_position]
                if new_position != 0:
                    if property.player is None and player.balance >= property.sale_value:
                        self.make_buy_according_to_conduct_player(property, player)

                    elif property.player and property.player != player:
                        player.balance -= property.rent_value
                self.properties[new_position] = property

                if self.is_completed_round(new_position):
                    player.balance += 100.00

                if player.balance <= 0.0:
                    self.remove_player_properties(player)
                    self.eliminated_players.append(player)
                self.players[index_player] = player

            if len(self.eliminated_players) == 3:
                self.winner = player
                break
            elif match_counter == MAXIMUM_AMOUNT_OF_MATCHES:
                self.discover_winner()
                self.timeout = 1

            match_counter += 1

        return SimulationResult(player=self.winner, timeout=self.timeout)

    def remove_player_properties(self, player: Player) -> None:
        for index_property in range(0, len(self.properties)):
            if self.properties[index_property].player == player:
                self.properties[index_property].player = None

    def get_new_player_position(self, current_position: int) -> int:
        end_position = len(self.properties)
        rolldice = self.roll_dice()
        new_position = current_position + rolldice
        if new_position == end_position:
            new_position = 0
        if new_position > end_position:
            new_position = new_position - end_position - 1
        return new_position

    def is_completed_round(self, new_position: int) -> bool:
        if new_position >= len(self.properties):
            return True
        return False

    def make_buy_according_to_conduct_player(self, property: Property, player: Player) -> None:
        if player.conduct == PlayerConduct.IMPULSIVE:
            property.player = player
            player.balance -= property.sale_value
        elif player.conduct == PlayerConduct.DEMANDING and 50.0 < property.rent_value <= player.balance:
            property.player = player
            player.balance -= property.sale_value
        elif player.conduct == PlayerConduct.CAUTIOUS and player.balance - property.sale_value >= 80.0:
            property.player = player
            player.balance -= property.sale_value
        elif player.conduct == PlayerConduct.RANDOM and self.get_probability_50_percent():
            property.player = player
            player.balance -= property.sale_value

    def discover_winner(self) -> None:
        matches = [player for player in self.players if player not in self.eliminated_players]
        self.winner = max(matches, key=lambda k: k.rounds)

    @staticmethod
    def get_probability_50_percent():
        return choice([True, False])

    @staticmethod
    def roll_dice():
        return randint(1, 6)
