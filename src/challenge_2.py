from types import NoneType

from src.utils import read_file

WEIGHT = {"X": 1, "Y": 2, "Z": 3}  # Rock (A)  # Paper (B)  # Scissors (C)
OPPONENT_CHOICES = {"A": "Rock", "B": "Paper", "C": "Scissors"}
YOUR_CHOICES = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
WIN_MAPPING = [("A", "Y"), ("B", "Z"), ("C", "X")]
LOST = 0
DRAW = 3
WIN = 6


def _get_round_score(round_result: int, choice: str):
    return round_result + WEIGHT.get(choice)


def execute_challenge_part_1(
    rps_tournament_results: list[dict],
) -> NoneType:
    tournament_result = sum(
        [
            _get_round_score(WIN, result[1])
            if result in WIN_MAPPING
            else _get_round_score(DRAW, result[1])
            if OPPONENT_CHOICES.get(result[0]) == YOUR_CHOICES.get(result[1])
            else _get_round_score(LOST, result[1])
            for result in rps_tournament_results
        ]
    )

    print(f"Your final score is {tournament_result}")


# def execute_challenge_part_2(
#     sum_of_carried_calories_by_elf: list[int],
# ) -> NoneType:
#     top_three = _get_top_three(sum_of_carried_calories_by_elf)
#
#     print(
#         f"The top three elves with more carried calories are {top_three} "
#         f"and the sum of calories are {sum(top_three):,} calories."
#     )


def _get_rps_tournament_results(rps_tournament_results: str) -> list[tuple]:
    return [
        tuple(result.split(" "))
        for result in rps_tournament_results.split("\n")
        if result
    ]


def execute_challenge() -> NoneType:
    """

    :return the number of calories carried by the elf who is carrying the
    highest number of calories.
    The method uses a file (../resources/challenge_1__input.txt) containing all
    calories carried by all elves, each line representing the number of
    calories and when there are two lines separating the numbers,
    it represents that the following calories were carried by another elf.
    """

    rps_tournament_results: str = read_file(
        "../resources/challenge_2__input.txt"
    )

    rps_tournament_results = _get_rps_tournament_results(
        rps_tournament_results
    )

    execute_challenge_part_1(rps_tournament_results)
    # execute_challenge_part_2(sum_of_carried_calories_by_elf)
    pass


if __name__ == "__main__":
    execute_challenge()
