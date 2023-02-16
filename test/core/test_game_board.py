from unittest import mock

from core.game_board import GameBoard
from models.player import Player, PlayerConduct


@mock.patch("core.game_board.MAXIMUM_AMOUNT_OF_MATCHES", 1)
def test_must_start_game():
    game_board = GameBoard()
    game_board.eliminated_players.extend([game_board.players[0], game_board.players[1], game_board.players[2]])
    result = game_board.start_game()

    assert result.timeout == 0
    assert result.player.conduct == game_board.players[3].conduct
    assert result.player.balance == 300.0
    assert result.player.rounds == 1


def test_must_remove_player_properties():
    player = Player(conduct=PlayerConduct.RANDOM)
    game_board = GameBoard()
    game_board.properties[0].player = Player(conduct=PlayerConduct.RANDOM)
    assert game_board.properties[0].player == player

    game_board.remove_player_properties(player)
    assert game_board.properties[0].player is None


@mock.patch("core.game_board.GameBoard.roll_dice")
def test_must_get_new_player_position_major(mock_roll_dice):
    mock_roll_dice.return_value = 2
    game_board = GameBoard()

    new_position = game_board.get_new_player_position(2)
    assert new_position == 4


@mock.patch("core.game_board.GameBoard.roll_dice")
def test_must_get_new_player_position_0(mock_roll_dice):
    mock_roll_dice.return_value = 18
    game_board = GameBoard()

    new_position = game_board.get_new_player_position(2)
    assert new_position == 0


@mock.patch("core.game_board.GameBoard.roll_dice")
def test_must_get_new_player_position_minor(mock_roll_dice):
    mock_roll_dice.return_value = 20
    game_board = GameBoard()

    new_position = game_board.get_new_player_position(2)
    assert new_position == 1


def test_must_is_completed_round_true():
    game_board = GameBoard()

    is_completed_round = game_board.is_completed_round(20)

    assert is_completed_round is True


def test_must_is_completed_round_false():
    game_board = GameBoard()

    is_completed_round = game_board.is_completed_round(19)

    assert is_completed_round is False


@mock.patch("core.game_board.GameBoard.get_probability_50_percent")
def test_must_make_buy_according_to_conduct_player_random(mock_get_probability_50_percent):
    mock_get_probability_50_percent.return_value = True
    player = Player(conduct=PlayerConduct.RANDOM)
    game_board = GameBoard()
    game_board.properties[0].sale_value = 10.5

    assert player.balance == 300.0
    assert game_board.properties[0].player is None

    game_board.make_buy_according_to_conduct_player(game_board.properties[0], player)

    assert player.balance == 289.5
    assert game_board.properties[0].player == player


def test_must_make_buy_according_to_conduct_player_cautious():
    player = Player(conduct=PlayerConduct.CAUTIOUS)
    game_board = GameBoard()
    game_board.properties[0].sale_value = 220.0

    assert player.balance == 300.0
    assert game_board.properties[0].player is None

    game_board.make_buy_according_to_conduct_player(game_board.properties[0], player)

    assert player.balance == 80.0
    assert game_board.properties[0].player == player


def test_must_make_buy_according_to_conduct_player_demanding():
    player = Player(conduct=PlayerConduct.DEMANDING)
    game_board = GameBoard()
    game_board.properties[0].rent_value = 51.0
    game_board.properties[0].sale_value = 299.0

    assert player.balance == 300.0
    assert game_board.properties[0].player is None

    game_board.make_buy_according_to_conduct_player(game_board.properties[0], player)

    assert player.balance == 1.0
    assert game_board.properties[0].player == player


def test_must_make_buy_according_to_conduct_player_impulsive():
    player = Player(conduct=PlayerConduct.IMPULSIVE)
    game_board = GameBoard()
    game_board.properties[0].sale_value = 301.0

    assert player.balance == 300.0
    assert game_board.properties[0].player is None

    game_board.make_buy_according_to_conduct_player(game_board.properties[0], player)

    assert player.balance == -1.0
    assert game_board.properties[0].player == player


def test_must_get_probability_50_percent():
    game_board = GameBoard()
    choice = game_board.get_probability_50_percent()

    assert choice in (True, False)


def test_must_roll_dice():
    game_board = GameBoard()
    values = game_board.roll_dice()

    assert values in (1, 2, 3, 4, 5, 6)
