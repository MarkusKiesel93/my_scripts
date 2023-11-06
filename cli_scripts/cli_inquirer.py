import inquirer
import datetime
import sys
from curtsies import Input


def ask_date():
    """
    inquires user four date
    navigate with ARROW UP, ARROW DOWN and RETURN KEY
    returns datetime date object
    """
    today = datetime.date.today()
    days_delta = 0
    print('date:')
    date = today
    sys.stdout.write(f'\r{date}')
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == 'KEY_UP':  # ARROW UP
                days_delta += 1
            if e == 'KEY_DOWN':  # ARROW DOWN
                days_delta -= 1
            if e == '\n':  # RETURN KEY
                break
            date = today - datetime.timedelta(days=days_delta)
            sys.stdout.write(f'\r{date}')
    print('')
    return date


def ask_string(prompt_message):
    """
    inquires user for some string
    prompt_message: message prompted to the user
    returns user Input as String
    """
    while True:
        item = input(f'{prompt_message}:\n')
        if _satisfying_answer(item):
            break
    return str(item)


def ask_float(prompt_message):
    """
    inquires user for some float value
    prompt_message: message prompted to the user
    returns user Input as Float
    """
    amount = None
    while type(amount) is not float:
        try:
            amount = input(f'{prompt_message}:\n')
            amount = float(amount)
        except ValueError:
            print(f'{prompt_message} has to be given as float')
    return amount


def ask_choices(name, choices, message, ask_new=False):
    """
    inquires user to selet one of the given choices
    if ask_new is True the user can select adding a new option
    returns user choice as String
    """
    answer = None
    if len(choices) < 1:
        raise Exception('at least one choice has to be given')
    if ask_new:
        choices.insert(0, 'new')
    questions = [inquirer.List(name, message=message, choices=choices)]
    ask_question = inquirer.prompt(questions)
    if ask_question and name in ask_question:
        answer = ask_question[name]
    if ask_new and answer == 'new':
        answer = ask_string(name)
    return answer


# check user input
def _satisfying_answer(answer):
    if len(answer) < 3:
        print('needs input of at least 3 characters!')
        return False
    return True
