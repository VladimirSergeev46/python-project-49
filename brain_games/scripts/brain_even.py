#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic
from brain_games.games.question import rand_num


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    logic(name, rand_num())


if __name__ == ' __main__':
    main()
