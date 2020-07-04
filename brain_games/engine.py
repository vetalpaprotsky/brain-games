import brain_games.cli as cli
import prompt


def ask_question_to_user(question):
    print('Question: %s' % question)
    return prompt.string('Your answer: ').strip().lower()


def start_game_loop(game, user_name):
    ANSWERS_TO_WIN_COUNT = 3
    correct_answers_count = 0

    while correct_answers_count < ANSWERS_TO_WIN_COUNT:
        question, correct_answer = game.get_question_and_correct_answer()
        correct_answer = str(correct_answer)
        user_answer = ask_question_to_user(question)

        if user_answer == correct_answer:
            correct_answers_count += 1
            print('Correct!')
        else:
            message = (
                "'%s' is wrong answer ;(. "
                "Correct answer was '%s'\n"
                "Let's try again, %s!"
            )
            print(message % (user_answer, correct_answer, user_name))

    print('Congratulations, %s!' % user_name)


def start(game):
    cli.show_greeting_message()
    print(game.RULES, '\n')
    user_name = cli.welcome_user()
    print()
    start_game_loop(game, user_name)
