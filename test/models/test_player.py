import random

from models.player import Player, PlayerConduct


def test_must_create_player():
    player = Player.create_player(conduct=random.choice(list(PlayerConduct)))
    assert player.conduct in list(PlayerConduct)
    assert player.current_position == 0
    assert player.balance == 300
    assert player.rounds == 0


def test_must_create_players():
    players = Player.create_players()
    assert len(players) == 4
    for player in players:
        assert player.conduct in list(PlayerConduct)
        assert player.current_position == 0
        assert player.balance == 300
        assert player.rounds == 0
