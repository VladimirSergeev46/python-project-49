#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.logic import logic


def main():
    logic(welcome_user())


if __name__ == ' __main__':
    main()
