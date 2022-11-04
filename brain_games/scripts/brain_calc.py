#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic
from brain_games.games.calc import rand_calc


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    logic(name, rand_calc())


if __name__ == ' __main__':
    main()
