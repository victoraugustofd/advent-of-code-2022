from types import NoneType

from src.utils import read_file


def _get_top_three(list_of_ints: list[int]) -> tuple[int]:
    return tuple(sorted(list_of_ints, reverse=True)[:3])


def execute_challenge_part_1(
    sum_of_carried_calories_by_elf: list[int],
) -> NoneType:
    print(
        f"The elf with more carried calories carry "
        f"{max(sum_of_carried_calories_by_elf):,} calories."
    )


def execute_challenge_part_2(
    sum_of_carried_calories_by_elf: list[int],
) -> NoneType:
    top_three = _get_top_three(sum_of_carried_calories_by_elf)

    print(
        f"The top three elves with more carried calories are {top_three} "
        f"and the sum of calories are {sum(top_three):,} calories."
    )


def execute_challenge() -> NoneType:
    """

    :return the number of calories carried by the elf who is carrying the
    highest number of calories.
    The method uses a file (../resources/challenge_1__input.txt) containing all
    calories carried by all elves, each line representing the number of
    calories and when there are two lines separating the numbers,
    it represents that the following calories were carried by another elf.
    """
    elves_carried_calories: str = read_file(
        "../resources/challenge_1__input.txt"
    )

    carried_calories_by_elf = _get_carried_calories_by_elf(
        elves_carried_calories
    )
    sum_of_carried_calories_by_elf = _get_sum_of_carried_calories_by_elf(
        carried_calories_by_elf
    )

    execute_challenge_part_1(sum_of_carried_calories_by_elf)
    execute_challenge_part_2(sum_of_carried_calories_by_elf)


def _get_sum_of_carried_calories_by_elf(
    carried_calories_by_elf: list[list[str]],
) -> list[int]:
    return [
        sum([int(calorie) for calorie in calories if calorie])
        for calories in carried_calories_by_elf
    ]


def _get_carried_calories_by_elf(
    elves_carried_calories: str,
) -> list[list[str]]:
    return [
        calories.split("\n")
        for calories in elves_carried_calories.split("\n\n")
    ]


if __name__ == "__main__":
    execute_challenge()
