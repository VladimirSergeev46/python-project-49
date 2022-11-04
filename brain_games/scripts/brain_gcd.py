#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic
from brain_games.games.gcd import rand_gcd


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    logic(name, rand_gcd())


if __name__ == ' __main__':
    main()
