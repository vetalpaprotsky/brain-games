import random


RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_correct_answer():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    # The number itself is a question
    return number, correct_answer
