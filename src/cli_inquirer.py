import inquirer
import datetime
import sys
from curtsies import Input

# TODO: add output messages as function arguments


def ask_date():
    today = datetime.date.today()
    days_delta = 0
    print('date:')
    # output in same line
    date = today
    sys.stdout.write(f'\r{date}')
    # use curtsies for Key input
    # decrese date with KEY_UP, incrise date with KEY_DOWN
    # select with return
    with Input(keynames='curses') as input_generator:
        for e in input_generator:
            if e == 'KEY_UP':
                days_delta += 1
            if e == 'KEY_DOWN':
                days_delta -= 1
            if e == '\n':
                break
            date = today - datetime.timedelta(days=days_delta)
            sys.stdout.write(f'\r{date}')
    print('')
    return date


# TODO: only use input once
def ask_string(prompt_name):
    item = input(f'{prompt_name}:\n')
    while len(item) <= 1:
        print(f'{prompt_name} needs to be given!')
        item = input(f'{prompt_name}:\n')
    return item


def ask_float(prompt_name):
    amount = None
    while type(amount) is not float:
        try:
            amount = input(f'{prompt_name}:\n')
            amount = float(amount)
        except ValueError:
            print(f'{prompt_name} has to be given as float')
    return amount


# TODO: not tested and not used
def ask_choices(name, choices, message):
    questions = [inquirer.List(name, message=message, choices=choices)]
    answers = inquirer.prompt(questions)
    return answers[name]
