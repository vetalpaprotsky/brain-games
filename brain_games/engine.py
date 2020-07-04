import brain_games.cli as cli


def start_game_loop(game, user_name):
    ANSWERS_TO_WIN_COUNT = 3
    correct_answers_count = 0

    while correct_answers_count < ANSWERS_TO_WIN_COUNT:
        user_answer, correct_answer = game.ask_question()

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
    game.show_game_rules()
    print()
    user_name = cli.welcome_user()
    print()
    start_game_loop(game, user_name)
