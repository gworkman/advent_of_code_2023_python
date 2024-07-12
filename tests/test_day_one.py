from advent_of_code.day_one import DayOne


class TestDayOne:
    def test_decode_lines_to_numbers_simple(self):
        line = "1abc2"
        answer = 12
        assert DayOne().decode_line_to_number(line) == answer

    def test_decode_lines_to_numbers_long(self):
        line = "pqr3stu8vwx"
        answer = 38
        assert DayOne().decode_line_to_number(line) == answer

    def test_decode_lines_to_numbers_multiple(self):
        line = "a1b2c3d4e5f"
        answer = 15
        assert DayOne().decode_line_to_number(line) == answer

    def test_decode_lines_to_numbers_single(self):
        line = "treb7uchet"
        answer = 77
        assert DayOne().decode_line_to_number(line) == answer

    def test_insert_spelled_digits_simple(self):
        line = "two1nine"
        answer = "2wo19ine"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_insert_spelled_digits_with_conflict(self):
        line = "eightwothree"
        answer = "8igh2wo3hree"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_insert_spelled_digits_with_padding(self):
        line = "abcone2threexyz"
        answer = "abc1ne23hreexyz"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_insert_spelled_digits_with_conflict_with_padding(self):
        line = "zoneight234"
        answer = "z1n8ight234"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_insert_spelled_digits_with_duplicates(self):
        line = "onemasone"
        answer = "1nemas1ne"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_insert_spelled_digits_with_duplicates_with_conflict(self):
        line = "eighthree"
        answer = "8igh3hree"
        assert DayOne().insert_spelled_digits(line) == answer

    def test_part_one(self):
        lines = "\n".join(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"])
        assert DayOne().part_one(lines) == 142

    def test_part_two(self):
        lines = "\n".join(
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen",
            ]
        )

        assert DayOne().part_two(lines) == 281
