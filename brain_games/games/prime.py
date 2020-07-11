import random
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    n = 2
    squareRootOfNumber = math.floor(math.sqrt(number))

    while n <= squareRootOfNumber:
        if number % n == 0:
            return False
        n += 1

    return True


def generate_number():
    '''
    The function tries to generate a prime number. Most likely that a random
    number isn't going to be prime. That makes the game a bit boring. That's why
    this function has more than one attempt to generate a number which might
    be a prime one.
    '''

    attemps_left = 3

    while attemps_left > 0:
        number = random.randint(1, 100)
        if is_prime(number):
            return number, True
        attemps_left -= 1

    return number, False


def get_question_and_correct_answer():
    number, number_is_prime = generate_number()
    correct_answer = 'yes' if number_is_prime else 'no'

    # The number itself is a question
    return number, correct_answer
