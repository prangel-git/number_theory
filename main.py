from numbertheory.src.utilities import *

from numbertheory.src.utilities import *
from numbertheory.src.chapter2 import *
from numbertheory.src.chapter3 import *
from numbertheory.src.chapter4 import *
from numbertheory.src.chapter5 import *


def main():
    bound = 1_500_000
    sum_squares_to_num_representations = exercise_5_26(bound)
    num_solutions = len(sum_squares_to_num_representations)

    print(
        f"there are {num_solutions} numbers smaller than {bound} that can be written as sum of squares"
    )

    request = (5**3) * 13 * 17 * 29
    print(
        f"{request} can be written in {sum_squares_to_num_representations[request]} ways"
    )


if __name__ == "__main__":
    main()
