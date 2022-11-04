import random
import math


def rand_prime():
    count = 0
    result = ()
    for _ in range(3):
        randon_number = random.randint(0, 200)
        for i in range(1, int(math.sqrt(randon_number))):
            if randon_number % i == 0:
                count += 1
            if count > 1:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
        question = randon_number
        result += (question, correct_answer),
    return result
