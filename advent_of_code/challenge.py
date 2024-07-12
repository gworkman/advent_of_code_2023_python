from typing import Any
from advent_of_code import utils
import time
import abc


class Challenge:
    def __init__(self):
        self.challenge_number = 0

    def solve(self):
        file_input = utils.get_file(self.challenge_number)

        start_time = time.time()
        part_one_solution = self.part_one(file_input)
        part_two_solution = self.part_two(file_input)
        end_time = time.time()

        print(f"Calculated solution in {end_time - start_time:0.3f} seconds")
        print(f"Part one: {part_one_solution}")
        print(f"Part two: {part_two_solution}")

    @abc.abstractmethod
    def part_one(self, input: str) -> Any:
        pass

    @abc.abstractmethod
    def part_two(self, input: str) -> Any:
        pass
