import random
import math


RULES = 'Find the greatest common divisor of given numbers.'


def generate_numbers():
    '''
    Try to generate numbers which have greatest common divisor greater than one.
    '''

    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100

    first_number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    attemps_count = 5

    while attemps_count > 0:
        second_number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
        if math.gcd(first_number, second_number) > 1:
            break
        attemps_count -= 1

    return first_number, second_number


def get_question_and_correct_answer():
    first_number, second_number = generate_numbers()
    question = '{} {}'.format(first_number, second_number)
    correct_answer = math.gcd(first_number, second_number)

    return question, correct_answer
