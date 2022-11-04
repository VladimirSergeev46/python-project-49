import random


operands = ('+', '-', '*')


def rand_calc():
    result = ()
    for _ in range(3):
        random_integer1 = random.randint(0, 100)
        random_integer2 = random.randint(0, 10)
        random_operand = operands[random.randint(0, 2)]
        question = f"{random_integer1} {random_operand} {random_integer2}"
        if random_operand == '+':
            correct_answer = random_integer1 + random_integer2
        elif random_operand == '-':
            correct_answer = random_integer1 - random_integer2
        elif random_operand == '*':
            correct_answer = random_integer1 * random_integer2
        result += (question, correct_answer),
    return result
