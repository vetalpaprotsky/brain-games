import brain_games.cli as cli
import random
import prompt


def show_game_rules():
    print('Answer "yes" if number even otherwise answer "no".')


def is_answer_correct(answer, number):
    return (
        (number % 2 == 0 and answer == 'yes') or
        (number % 2 == 1 and answer == 'no')
    )


def get_opposite_answer(answer):
    return 'yes' if answer == 'no' else 'no'


def start_game_loop(user_name):
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100
    ANSWERS_TO_WIN_COUNT = 3
    correct_answers_count = 0

    while correct_answers_count < ANSWERS_TO_WIN_COUNT:
        number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
        print('Question: %s' % number)
        user_answer = prompt.string('Your answer: ')

        if is_answer_correct(user_answer, number):
            correct_answers_count += 1
            print('Correct!')
        else:
            message = (
                "'%s' is wrong answer ;(. "
                "Correct answer was '%s'\n"
                "Let's try again, %s!"
            )
            correct_answer = get_opposite_answer(user_answer)
            print(message % (user_answer, correct_answer, user_name))

    print('Congratulations, %s!' % user_name)


def start():
    cli.show_greeting_message()
    show_game_rules()
    print()
    user_name = cli.welcome_user()
    print()
    start_game_loop(user_name)
