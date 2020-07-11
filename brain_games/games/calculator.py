import random
import operator


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_correct_answer():
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 25
    OPERATIONS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    first_operand = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    second_operand = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    operation = random.choice(list(OPERATIONS))
    question = '{} {} {}'.format(first_operand, operation, second_operand)
    correct_answer = OPERATIONS[operation](first_operand, second_operand)

    return question, correct_answer
