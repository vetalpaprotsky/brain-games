import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(first_number, step, length):
    last_number = first_number + length * step
    progression = list(range(first_number, last_number, step))

    return progression


def get_question_and_correct_answer():
    PROG_LENGTH = 10
    PROG_STEP = random.randint(1, 10)
    PROG_FIRST_NUM = random.randint(1, 100)
    progression = generate_progression(PROG_FIRST_NUM, PROG_STEP, PROG_LENGTH)
    random_element_index = random.randint(0, PROG_LENGTH - 1)
    correct_answer = progression[random_element_index]
    progression[random_element_index] = '..'
    # In order to join integers and string into single string, all integers
    # need to be converted into string first and only then list can be joined.
    question = ' '.join(map(str, progression))

    return question, correct_answer
