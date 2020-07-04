import random


RULES = 'Answer "yes" if number even otherwise answer "no".'


def get_question_and_correct_answer():
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100

    # The number itself is a question
    number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return number, correct_answer
