import random


def rand_num():
    result = ()
    for _ in range(3):
        random_integer = random.randint(1, 100)
        if random_integer % 2 == 0:
            correct_answer = 'yes'
        elif random_integer % 2 != 0:
            correct_answer = 'no'
        result += (random_integer, correct_answer),
    return result
