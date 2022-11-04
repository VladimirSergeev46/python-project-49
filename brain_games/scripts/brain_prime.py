#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic
from brain_games.games.prime import rand_prime


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    logic(name, rand_prime())


if __name__ == ' __main__':
    main()
