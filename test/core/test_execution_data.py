from core.execution_data import ExecutionData
from models.player import Player, PlayerConduct
from models.simulation_result import SimulationResult


def get_execution_data():
    simulations_result = [
        SimulationResult(player=Player(conduct=PlayerConduct.RANDOM, rounds=200), timeout=0),
        SimulationResult(player=Player(conduct=PlayerConduct.CAUTIOUS, rounds=150), timeout=1),
    ]

    return ExecutionData(simulations_result)


def test_must_get_number_matches_timeout():
    execution_data = get_execution_data()
    matches_timeout = execution_data.get_number_matches_timeout()
    assert matches_timeout == 1


def test_must_get_average_rounds_by_game():
    execution_data = get_execution_data()
    average_rounds_by_game = execution_data.get_average_rounds_by_game()
    assert average_rounds_by_game == 175.0


def test_must_get_winning_percentage_by_player():
    execution_data = get_execution_data()
    max_winner_conduct = execution_data.get_winning_percentage_by_player()
    assert max_winner_conduct == PlayerConduct.CAUTIOUS.value
