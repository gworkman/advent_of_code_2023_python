from typing import Dict

from advent_of_code.challenge import Challenge


class DayTwo(Challenge):
    def __init__(self):
        self.challenge_number = 2

    def part_one(self, input: str) -> int:
        lines = input.splitlines()
        games = {
            self.game_line_to_game_id(line): self.game_line_to_max_cube_colors(line)
            for line in lines
        }

        game_conditions = {"red": 12, "green": 13, "blue": 14}

        valid_ids = [
            id
            for id, game in games.items()
            if self.game_is_possible(game, game_conditions)
        ]

        return sum(valid_ids)

    def part_two(self, input: str) -> int:
        lines = input.splitlines()
        games = {
            self.game_line_to_game_id(line): self.game_line_to_max_cube_colors(line)
            for line in lines
        }

        powers = [game["red"] * game["green"] * game["blue"] for game in games.values()]
        return sum(powers)

    def game_line_to_game_id(self, line: str) -> int:
        """
        Parses the game ID from the input string

        :param str line: the string containing the individual game info
        :return: the ID of the game
        """
        line = line.removeprefix("Game ")
        digit_end = line.find(":")
        game_id = int(line[:digit_end])
        return game_id

    def game_line_to_max_cube_colors(self, line: str) -> Dict[str, int]:
        """
        Aggregates the maximum number of cubes drawn for each color for the input game string

        :param str line: the string containing the individual game info
        :return: the maximum cubes drawn of each color, as a dict
        """
        data_start = line.find(":")

        max_cube_colors = {"red": 0, "green": 0, "blue": 0}

        for revealed_cubes in line[data_start + 1 :].split(";"):
            for cube_colors in revealed_cubes.split(", "):
                [amount_str, color] = cube_colors.removeprefix(" ").split(" ")
                amount = int(amount_str)

                if amount > max_cube_colors[color]:
                    max_cube_colors[color] = amount

        return max_cube_colors

    def game_is_possible(
        self, max_cube_colors: Dict[str, int], condition: Dict[str, int]
    ) -> bool:
        """
        Determines if the game was possible given the cube count condition

        :param dict[str, int] max_cube_colors: the maximum number of cubes drawn for each color during the game
        :param dict[str, int] condition: the conditions of the game
        :return: whether or not the game was possible
        """
        for color in max_cube_colors.keys():
            if max_cube_colors[color] > condition[color]:
                return False

        return True
