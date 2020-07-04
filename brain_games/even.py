import brain_games.cli as cli
import random
import prompt


def show_game_rules():
    print('Answer "yes" if number even otherwise answer "no".')


def is_answer_correct(number, answer):
    return (
        (number % 2 == 0 and answer == 'yes') or
        (number % 2 == 1 and answer == 'no')
    )


def get_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def ask_question():
    LOWEST_RAND_NUM = 1
    BIGGEST_RAND_NUM = 100

    asked_number = random.randint(LOWEST_RAND_NUM, BIGGEST_RAND_NUM)
    print('Question: %s' % asked_number)
    user_answer = prompt.string('Your answer: ')

    return asked_number, user_answer


def start_game_loop(user_name):
    ANSWERS_TO_WIN_COUNT = 3
    correct_answers_count = 0

    while correct_answers_count < ANSWERS_TO_WIN_COUNT:
        asked_number, user_answer = ask_question()

        if is_answer_correct(asked_number, user_answer):
            correct_answers_count += 1
            print('Correct!')
        else:
            message = (
                "'%s' is wrong answer ;(. "
                "Correct answer was '%s'\n"
                "Let's try again, %s!"
            )
            correct_answer = get_correct_answer(asked_number)
            print(message % (user_answer, correct_answer, user_name))

    print('Congratulations, %s!' % user_name)


def start():
    cli.show_greeting_message()
    show_game_rules()
    print()
    user_name = cli.welcome_user()
    print()
    start_game_loop(user_name)
