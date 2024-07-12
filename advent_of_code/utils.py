import requests
import os

AOC_COOKIE = os.getenv("AOC_COOKIE")

if AOC_COOKIE == "":
    raise RuntimeWarning("AOC_COOKIE was not found in the current environment")


def get_file(challenge_number: int, year: int = 2023) -> str:
    """
    Gets the file input for the AOC challenge

    :param int challenge_number: the challenge number to fetch the file input for
    """

    if challenge_number <= 0 or challenge_number > 25:
        raise IndexError("Challenge number outside range [1, 25]")

    cookies = {"session": AOC_COOKIE}
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{challenge_number}/input", cookies=cookies
    )

    if resp.status_code != 200:
        raise RuntimeError("Unable to get the input. Try refreshing the cookie")

    return resp.text
