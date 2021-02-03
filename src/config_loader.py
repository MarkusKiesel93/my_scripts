import yaml
from pathlib import Path


CONFIG_PATH = Path(__file__).parent.parent / 'configs'


class ConfigLoader:
    def get(self, config_name):
        """
        returns the specifyed config as dictionary
        """
        config_file_path = self._create_path(config_name)
        return self._load_config(config_file_path)

    def _load_config(self, config_file_path):
        with open(config_file_path, 'r') as cfg_file:
            cfg = yaml.safe_load(cfg_file)
        return cfg

    def _create_path(self, config_name):
        file_name = ''.join([config_name, '.yml'])
        file_path = (CONFIG_PATH / file_name).resolve()
        if not file_path.exists():
            raise Exception(f'no config file with name: {config_name}')
        return file_path.as_posix()
