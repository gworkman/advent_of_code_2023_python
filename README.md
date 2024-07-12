# Advent of Code 2023

This repo serves as a framework of utilities and solutions for the AOC 2023 challenges, written in Python.

The solutions are written with test-driven development to ensure good test coverage. 

## Installation

Poetry is used to manage the Python environment and dependencies. After cloning the repo, run `poetry install`.

Additionally, the Advent of Code session must be exported in the `AOC_COOKIE` environment variable if you wish to download your file input at runtime, rather than using a local file.

## Usage

To solve for a specific day's challenge, run `poetry run python -m advent_of_code --day DAY_NUMBER`.
