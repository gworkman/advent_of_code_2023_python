import advent_of_code
import argparse

parser = argparse.ArgumentParser(
    prog="advent_of_code",
    usage="python -m advent_of_code --day 1",
    description="Advent of Code solver by Gus Workman",
)

parser.add_argument("-d", "--day", type=int, required=True)
args = parser.parse_args()

# get the module from the exports listed in __init__.py
challenge_module_str = advent_of_code.__all__[args.day - 1]
challenge_module = getattr(advent_of_code, challenge_module_str)

# run the module and print results
challenge_module().solve()
