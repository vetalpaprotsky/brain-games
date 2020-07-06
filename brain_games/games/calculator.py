import random


RULES = 'What is the result of the expression?'


def get_question_and_correct_answer():
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 25
    OPERATIONS = ['+', '-', '*']
    first_operand = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    second_operand = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    operation = random.choice(OPERATIONS)
    question = '{} {} {}'.format(first_operand, operation, second_operand)

    if operation == '+':
        correct_answer = first_operand + second_operand
    elif operation == '-':
        correct_answer = first_operand - second_operand
    else:
        correct_answer = first_operand * second_operand

    return question, correct_answer
