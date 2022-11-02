import random


def rand_num():
    random_integer = random.randint(1, 100)
    if random_integer % 2 == 0:
        correct_answer = 'yes'
    elif random_integer % 2 != 0:
        correct_answer = 'no'
    return random_integer, correct_answer
