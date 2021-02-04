import pandas as pd
import datetime

from src.db_path_loader import DbPathLoader
from src.cli_inquirer import ask_date, ask_string, ask_float

class DebtTracker():
    def __init__(self):
        self.db_path = DbPathLoader().get('debt')
        self.db = pd.read_csv(self.db_path)

    def add(self):
        new_debt = {'person':'','amount':'','purpose':'','date':''}
        new_debt['date'] = ask_date()
        new_debt['person'] = ask_string('person')
        new_debt['amount'] = ask_float('amount')
        new_debt['purpose'] = ask_string('purpose')
        self.db = self.db.append(new_debt, ignore_index=True)
        self.__save_db()

    def info(self, person = None):
        persons = list(self.db.person.unique())
        amounts = self.db.groupby('person').sum()
        for person in persons:
            amount = amounts.loc[person, 'amount']
            print(f'{person}: {amount:.2f}')

    def list(self, person):
        pd.set_option('display.max_rows', None)
        print(self.db[self.db.person == person])

    def __save_db(self):
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        self.__info_after_save()

    def __info_after_save(self):
        print('\nSUCCESSFULLY ADDED DEBT TO DB\n')
        print(self.db.tail(10))
        self.info()
