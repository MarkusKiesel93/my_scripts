import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).parent.parent / 'configs'


class ConfigLoader:
    def __init__(self, private_path=None):
        self.private_path = private_path

    def get(self, config_name):
        """
        returns the specifyed config as dictionary
        """
        if not self.private_path:
            config_file_path = self._create_path(config_name)
        else:
            config_file_path = self.private_path
        return self._load_config(config_file_path)

    def _load_config(self, config_file_path):
        with open(config_file_path, 'r') as cfg_file:
            cfg = yaml.safe_load(cfg_file)
        return cfg

    def _create_path(self, config_name):
        file_name = ''.join([config_name, '.yml'])
        file_path = (CONFIG_PATH / file_name).resolve()
        if not file_path.exists():
            raise OSError(f'config file not found:\n {file_path}')
        return file_path.as_posix()
