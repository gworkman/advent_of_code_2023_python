from typing import List

from advent_of_code.challenge import Challenge

DIGIT_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class DayOne(Challenge):
    def __init__(self) -> None:
        self.challenge_number = 1

    def part_one(self, input: str) -> int:
        lines = input.splitlines()
        calibration_numbers = [self.decode_line_to_number(line) for line in lines]
        return sum(calibration_numbers)

    def part_two(self, input: str) -> int:
        lines = input.splitlines()
        lines = [self.insert_spelled_digits(line) for line in lines]
        calibration_numbers = [self.decode_line_to_number(line) for line in lines]
        return sum(calibration_numbers)

    def decode_line_to_number(self, line: str) -> int:
        """
        Decodes the line to the two-digit number as defined by the challenge: the first numerical
        digit of the line is placed in the tens place and the last numerical digit of the line
        is placed in the ones place. The first and last digit of the line may be the same digit,
        but this function requires at least one digit in the string.

        :param str line: the line to decode.
        :return: the decoded number from the line.
        """
        digits = [int(digit) for digit in line if digit.isdigit()]
        tens_digit = digits[0]
        ones_digit = digits[-1]

        return tens_digit * 10 + ones_digit

    def insert_spelled_digits(self, line: str) -> str:
        """
        Replaces the first letter of a spelled out digit with the ASCII number character corresponding to the digit.

        Example: "8ight" = insert_spelled_digits("eight")

        :param str line: the line to replace spelled digits in
        :return: modified line with the first letter of spelled digits replaced by the numerical digit
        """
        digit_indices = {
            spelled_digit: self.find_all_indices(line, spelled_digit)
            for spelled_digit in DIGIT_MAPPING.keys()
        }

        line_arr = list(line)

        for spelled_digit, indices in digit_indices.items():
            replace_value = DIGIT_MAPPING[spelled_digit]
            for index in indices:
                line_arr[index] = replace_value

        return "".join(line_arr)

    def find_all_indices(self, line: str, key: str) -> List[int]:
        """
        Finds all indices of occurance of a substring within a string.

        :param str line: the base string to find substrings within
        :param str key: the substring to find
        :return: a list of the indices of the substring within the string
        """
        indices = []
        start_index = 0
        while (str_index := line.find(key, start_index)) >= 0:
            indices.append(str_index)
            start_index = str_index + 1

        return indices
