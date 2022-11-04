import random


def rand_progression():
    sequence = []
    result = ()
    for _ in range(3):
        start_sequence = random.randint(0, 30)
        sequence = [start_sequence]
        count = random.randint(1, 20)
        for _ in range(10):
            start_sequence += count
            sequence.append(start_sequence)
        deleted_element = random.randint(0, len(sequence) - 1)
        correct_answer = sequence[deleted_element]
        sequence[deleted_element] = '..'
        question = sequence
        result += (question, correct_answer),
    return result
