import pandas as pd
from cli_scripts.config_loader import load_path
from cli_scripts.cli_inquirer import ask_date, ask_string, ask_float, ask_choices


class ExpenseTracker:
    def __init__(self):
        self.db_path = load_path('expenses')
        self.db = pd.read_csv(self.db_path)

    def add(self):
        """
        add a new expense to the data file
        inquires information from user
        """
        add_another = 'yes'
        while add_another == 'yes':
            self._ask_new_expense()
            add_another = ask_choices('finished', ['yes', 'no'], 'add another expense ?')
        self._save_db()
    
    def delete_last(self, n=1):
        """
        delete the last n rows from the data file
        """
        self.db.drop(self.db.tail(n).index, inplace=True)
        self._save_db()

    def list(self, n=10):
        """
        list the last n rows from the data file
        """
        print(self.db.tail(n))

    def _save_db(self):
        self.list()
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        print('successfully saved data')

    def _ask_new_expense(self):
        new_expense = {}
        new_expense['date'] = ask_date()
        new_expense['item'] = ask_string('item')
        new_expense['amount'] = ask_float('amount')
        choices = self.db[self.db.item == new_expense['item']].category.unique().tolist()
        if len(choices) > 0:
            new_expense['category'] = ask_choices('category', choices, 'category', ask_new=True)
        else:
            new_expense['category'] = ask_string('new category')
        self.db = self.db.append(new_expense, ignore_index=True)