from advent_of_code.day_two import DayTwo


class TestDayTwo:
    def test_game_line_to_game_id_single_digit(self):
        line = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        answer = 5
        assert DayTwo().game_line_to_game_id(line) == answer

    def test_game_line_to_game_id_double_digit(self):
        line = "Game 19: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        answer = 19
        assert DayTwo().game_line_to_game_id(line) == answer

    def test_game_line_to_game_id_triple_digit(self):
        line = "Game 912: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        answer = 912
        assert DayTwo().game_line_to_game_id(line) == answer

    def test_game_line_to_cube_counts(self):
        line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        result = {"red": 4, "green": 2, "blue": 6}
        assert DayTwo().game_line_to_max_cube_colors(line) == result

        line = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        result = {"red": 1, "green": 3, "blue": 4}
        assert DayTwo().game_line_to_max_cube_colors(line) == result

        line = (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        result = {"red": 20, "green": 13, "blue": 6}
        assert DayTwo().game_line_to_max_cube_colors(line) == result

    def test_part_one(self):
        lines = "\n".join(
            [
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ]
        )

        answer = 8

        assert DayTwo().part_one(lines) == answer

    def test_part_two(self):
        lines = "\n".join(
            [
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
                "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            ]
        )

        answer = 2286

        assert DayTwo().part_two(lines) == answer
