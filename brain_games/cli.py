import prompt

def welcome_user():
    print() # Adds empty line
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
