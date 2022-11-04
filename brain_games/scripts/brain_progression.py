#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic
from brain_games.games.progression import rand_progression


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    logic(name, rand_progression())


if __name__ == ' __main__':
    main()
