import prompt


def logic(name, question_answer):
    for i in range(3):
        question = question_answer[i][0]
        correct_answer = question_answer[i][1]
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
