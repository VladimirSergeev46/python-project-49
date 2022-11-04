import random
import math


def rand_gcd():
    result = ()
    for _ in range(3):
        random_integer1 = random.randint(0, 100)
        random_integer2 = random.randint(0, 10)
        correct_answer = math.gcd(random_integer1, random_integer2)
        question = f"{random_integer1} {random_integer2}"
        result += (question, correct_answer),
    return result
