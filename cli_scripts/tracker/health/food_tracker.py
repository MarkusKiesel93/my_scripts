import pandas as pd
from datetime import datetime

from configs.config_loader import load_path
from cli_scripts.cli_inquirer import ask_choices, ask_string


class FoodTracker:
    def __init__(self):
        self.db_path = load_path('food')
        self.db = pd.read_csv(self.db_path)

    def track(self):
        try:
            self._track()
        except KeyboardInterrupt:
            print('saving')
            self._save_db()

    def _track(self):
        finished = 'no'
        while finished == 'no':
            self._add()
            finished = ask_choices('finished', ['no', 'yes'], 'finished?')
        self._save_db()

    def _add(self):
        item = {}
        item['date'] = datetime.now().strftime('%Y-%m-%d')
        item['food'] = self._ask_food()
        item['processed'] = ask_choices('processed', ['yes', 'no'], 'processed?') == 'yes'
        self.db.loc[len(self.db)] = item

    def _ask_food(self):
        food_options = sorted(self.db.food.unique().tolist())
        if len(food_options) > 0:
            return ask_choices('food', food_options, 'food', ask_new=True)
        else:
            return ask_string('food')

    def _save_db(self):
        print(self.db.tail(10))
        self.db.to_csv(path_or_buf=self.db_path, index=False)
        print('successfully saved data')
