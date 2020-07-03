import prompt


def welcome_user():
    # Adds empty line
    print()
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
