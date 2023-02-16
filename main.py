from core.game_board import GameBoard
from settings import SIMULATIONS_EXECUTED

if __name__ == '__main__':
    simulations_result = []
    for _ in range(0, SIMULATIONS_EXECUTED):
        game_board = GameBoard()
        result = game_board.start_game()
        simulations_result.append(result)
