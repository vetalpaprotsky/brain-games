import random
import math


RULES = 'Find the greatest common divisor of given numbers.'


def generate_numbers():
    '''
    The function tries to generate numbers which have the greatest common
    divisor greater than one. Most likely that greatest common divisor of
    two random numbers is one. That makes the game a bit boring. That's why
    this function has more than one attempt to generate numbers which might
    be more interesting.
    '''

    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100
    first_number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    attemps_left = 5

    while attemps_left > 0:
        second_number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
        if math.gcd(first_number, second_number) > 1:
            break
        attemps_left -= 1

    return first_number, second_number


def get_question_and_correct_answer():
    first_number, second_number = generate_numbers()
    question = '{} {}'.format(first_number, second_number)
    correct_answer = math.gcd(first_number, second_number)

    return question, correct_answer
