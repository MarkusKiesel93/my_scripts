from pathlib import Path

from configs.config_loader import ConfigLoader

class DbPathLoader:
    """
    handles links to the my databases
    needs specifyed database home (db_home)
    and names for each database
    """
    def __init__(self):
        self.db_home_name = 'db_home'
        self.db_configs = ConfigLoader().get('databases')

    def get(self, db_name):
        """
        returns absolute path for database files as string
        """
        db_home = self._create_db_home()
        try:
            path = db_home / self.db_configs[db_name]
            return path.resolve().as_posix()
        except:
            raise KeyError(f'no db with name "{db_name}" in config file')

    def _create_db_home(self):
        home = Path().home()
        db_home = home / self.db_configs[self.db_home_name]
        if not db_home.exists():
            raise Exception(f'not able to access database home: {db_home}')
        return db_home

# test
if __name__=='__main__':
    d = DB_PATH()
    print(d.get('expenses'))
    print(d.get('asdf'))
