import random
from dataclasses import dataclass

from models.player import Player
from settings import (MAXIMUM_PROPERTY_RENT_VALUE, MAXIMUM_PROPERTY_SALE_VALUE,
                      MINIMIUM_PROPERTY_RENT_VALUE,
                      MINIMIUM_PROPERTY_SALE_VALUE, TOTAL_PROPERTIES)


@dataclass
class Property:
    sale_value: float = 0.0
    rent_value: float = 0.0
    player: Player = None

    @classmethod
    def create_property(cls):
        sale_value = random.uniform(MINIMIUM_PROPERTY_SALE_VALUE, MAXIMUM_PROPERTY_SALE_VALUE)
        rent_value = random.uniform(MINIMIUM_PROPERTY_RENT_VALUE, MAXIMUM_PROPERTY_RENT_VALUE)
        return cls(sale_value=sale_value, rent_value=rent_value)

    @staticmethod
    def create_game_board_properties() -> list:
        return list(map(lambda x: Property.create_property(), range(TOTAL_PROPERTIES)))
