from pathlib import Path
from .config_loader import ConfigLoader

PATH_CONFIG = 'my_paths'


class PathLoader:
    """
    handles links to the my data and private config files
    needs specifyed file home specifyed in "{PATH_CONFIG}.yml"
    and names for each file
    """
    def __init__(self):
        self.configs = ConfigLoader().get(PATH_CONFIG)

    def get(self, name):
        """
        returns absolute path for database files as string
        """
        home = self._create_files_home()
        try:
            path = home / self.configs[name]
            return path.resolve().as_posix()
        except Exception:
            raise KeyError(f'no setting for "{name}" in configs/{PATH_CONFIG}.yml')

    def _create_files_home(self):
        home = Path().home()
        files_home = home / self.configs['home']
        if not files_home.exists():
            raise OSError(f'private files home canno\'t be accessed:\n {files_home}')
        return files_home