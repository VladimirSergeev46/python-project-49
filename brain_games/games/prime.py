import random


def rand_prime():
    result = ()
    for _ in range(3):
        count = 0
        randon_number = random.randint(0, 200)
        for i in range(1, randon_number // 2 + 2):
            print(i, count)
            if randon_number % i == 0:
                count += 1
            if count > 1 or randon_number == 0 or randon_number == 1:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
        question = randon_number
        result += (question, correct_answer),
    return result
