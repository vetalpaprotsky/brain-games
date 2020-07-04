import random
import prompt


def show_game_rules():
    print('Answer "yes" if number even otherwise answer "no".')


def get_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def ask_question():
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100

    number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    print('Question: %s' % number)
    user_answer = prompt.string('Your answer: ')

    return user_answer, get_correct_answer(number)
