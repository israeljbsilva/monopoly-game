from models.player import Player, PlayerConduct
from models.simulation_result import SimulationResult


def test_must_create_simulation_result():
    simulation_result = SimulationResult(player=Player(conduct=PlayerConduct.RANDOM), timeout=2)
    assert simulation_result.player.conduct == PlayerConduct.RANDOM
    assert simulation_result.timeout == 2
