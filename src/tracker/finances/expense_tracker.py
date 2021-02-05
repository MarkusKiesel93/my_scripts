import pandas as pd
from src.config_loader import load_path
from src.cli_inquirer import ask_date, ask_string, ask_float, ask_choices


class ExpenseTracker:
    def __init__(self):
        self.db_path = load_path('expenses')
        self.db = pd.read_csv(self.db_path)

    def add(self):
        finished = False
        while not finished:
            self._ask_new_expense()
            message = 'add another expense ?'
            choices = ['yes', 'no']
            answer = ask_choices('finished', choices, message)
            if answer == 'no':
                finished = True
        self._save_db()

    def donate(self):
        self._ask_new_donation()
        self._save_db()

    def list(self, num_rows=10):
        print(self.db.tail(num_rows))

    def _save_db(self):
        self.list()
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        print('successfully added data')

    def _ask_new_expense(self):
        new_expense = {'date': '', 'item': '', 'place': '', 'amount': 0.0, 'category': '', 'sub_category': ''}
        new_expense['date'] = ask_date()
        new_expense['item'] = ask_string('item')
        new_expense['amount'] = ask_float('amount')
        new_expense['category'] = self._inquire_user('category', new_expense['item'])
        new_expense['sub_category'] = self._inquire_user('sub_category', new_expense['item'])
        new_expense['place'] = self._inquire_user('place', new_expense['item'])

        self.db = self.db.append(new_expense, ignore_index=True)

    def _ask_new_donation(self):
        new_expense = {'date': '', 'item': '', 'place': '', 'amount': 0.0, 'category': '', 'sub_category': ''}
        new_expense['date'] = ask_date()
        new_expense['item'] = 'donation'
        new_expense['amount'] = ask_float('amount')

        self.db = self.db.append(new_expense, ignore_index=True)

    def _inquire_user(self, column, item):
        choices = self._get_choices(column, item)
        message = column.replace('_', ' ')
        answer = ask_choices(column, choices, message)
        if answer == 'new':
            new = input(f'new {column.replace("_", " ")}:\n')
            return new
        elif answer == 'blank':
            return ''
        else:
            return answer

    def _get_choices(self, column, item):
        choices = self.db.query(f'item == "{item}"')
        choices = choices[column]
        choices = choices.drop_duplicates()
        choices = choices.dropna()
        choices = choices.tolist()
        choices += ['blank', 'new']
        return choices
