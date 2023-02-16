from dataclasses import dataclass

from models.player import Player


@dataclass
class SimulationResult:
    player: Player
    timeout: int
