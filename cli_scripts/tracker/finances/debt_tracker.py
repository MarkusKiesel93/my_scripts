import pandas as pd
from datetime import datetime, date
from configs.config_loader import load_config, load_path
from cli_scripts.cli_inquirer import ask_date, ask_string, ask_float, ask_choices


class DebtTracker():
    def __init__(self):
        self.new_debt = {'person':'','amount':'','purpose':'','date':''}
        self.db_path = load_path('debt')
        self.db = pd.read_csv(self.db_path)

    def add(self):
        """
        add a debt to the data file
        inquires information from user
        """
        self.new_debt['date'] = ask_date().strftime('%Y-%m-%d')
        persons = self.db.person.unique().tolist()
        if len(persons) > 0:
            self.new_debt['person'] = ask_choices('person', persons, 'person', ask_new=True)
        else:
            self.new_debt['person'] = ask_string('new category')
        self.new_debt['amount'] = ask_float('amount')
        self.new_debt['purpose'] = ask_string('purpose')
        self.db.loc[len(self.db)] = self.new_debt
        self._save_db()

    def info(self, person = None):
        """
        prints information per person
        person1: amount
        person2: amount
        ...
        """
        persons = list(self.db.person.unique())
        amounts = self.db.groupby('person').sum()
        for person in persons:
            amount = amounts.loc[person, 'amount']
            print(f'{person}: {amount:.2f}')

    def list(self, person):
        """
        lists all debts for one named person
        """
        pd.set_option('display.max_rows', None)
        print(self.db[self.db.person == person])

    def delete_last(self, n=1):
        """
        delete the last n rows from the data file
        """
        self.db.drop(self.db.tail(n).index, inplace=True)
        self._save_db()

    def periodic_debt(self):
        """
        adds a periodic debt from the config file to the data file
        only monthly periods are supported currently
        """
        p_debt = load_config('periodic_debt')
        this_month = datetime.today().month
        this_year = datetime.today().year
        for purpose in p_debt:
            debt_purpose = f'{purpose} {this_month}-{this_year}'
            if not (self.db.purpose == debt_purpose).any():
                for person, amount in p_debt[purpose]['per_person'].items():
                    self.new_debt['date'] = date(this_year, this_month, p_debt[purpose]['due_day'])
                    self.new_debt['person'] = person
                    self.new_debt['amount'] = amount
                    self.new_debt['purpose'] = debt_purpose
                    self.db = self.db.append(self.new_debt, ignore_index=True)
        self._save_db()

    def _save_db(self):
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        print(self.db.tail(10))
        self.info()
        print('successfully saved data')
