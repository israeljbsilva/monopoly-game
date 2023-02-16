from dataclasses import dataclass
from enum import Enum

from settings import INITIAL_BALANCE_PER_PLAYER


class PlayerConduct(Enum):
    IMPULSIVE = 'Impulsivo'
    DEMANDING = 'Exigente'
    CAUTIOUS = 'Cauteloso'
    RANDOM = 'Aleatório'


@dataclass
class Player:
    conduct: PlayerConduct
    current_position: int = 0
    balance: float = INITIAL_BALANCE_PER_PLAYER
    rounds: int = 0

    @classmethod
    def create_players(cls) -> list:
        return [cls.create_player(list(PlayerConduct)[index]) for index in range(len(PlayerConduct))]

    @staticmethod
    def create_player(conduct: PlayerConduct):
        return Player(conduct=conduct)
