from models.player import PlayerConduct


class ExecutionData:

    def __init__(self, simulations_result):
        self.simulations_result = simulations_result

    def get_number_matches_timeout(self) -> int:
        return len([result.timeout for result in self.simulations_result if result.timeout])

    def get_average_rounds_by_game(self) -> float:
        total_rounds = [result.player.rounds for result in self.simulations_result]
        return sum(total_rounds) / len(total_rounds)

    def get_winning_percentage_by_player(self) -> str:
        percentage_by_player = []
        conduct_by_player = []
        for conduct in PlayerConduct:
            total_conduct_player = len([result.player.conduct for result in self.simulations_result
                                        if result.player.conduct == conduct])
            percentage = total_conduct_player / len(self.simulations_result) * 100
            print(f'{conduct.value}: {percentage:.2f}%')
            conduct_by_player.append(conduct.value)
            percentage_by_player.append(percentage)

        return conduct_by_player[percentage_by_player.index(max(percentage_by_player))]
