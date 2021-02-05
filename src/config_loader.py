import yaml
from pathlib import Path

PRODUCTION = True

REPOSITORY_PATH = Path(__file__).parent.parent
CONFIG_PATH = REPOSITORY_PATH / 'configs'
EXAMPLE_PATH = REPOSITORY_PATH / 'examples'
PATH_CONFIG_FILE = 'my_paths'


def load_config(config_name, external=False):
    """
    returns the specifyed config as dictionary
    config has to be a yaml file with suffix ".yml"
    external: if config located outside the dedicated configs folder
        if external the path has to be specifyed in configs/my_paths.yml
    """
    config_folder_path = CONFIG_PATH
    if external and PRODUCTION:
        config_folder_path = load_path(config_name)
    if not PRODUCTION:
        config_folder_path = EXAMPLE_PATH
    config_file_path = (config_folder_path / config_name).with_suffix('.yml').resolve()
    if not config_file_path.exists():
        raise OSError(f'file not found:\n{config_file_path}')

    with open(config_file_path, 'r') as cfg_file:
        cfg = yaml.safe_load(cfg_file)
    return cfg


def load_path(name):
    """
    handles paths to external files
    name and path need to be specifyed in configs/my_paths.yml
    paths have to be relative from home and names must be unique
    """
    if PRODUCTION:
        configs = load_config(PATH_CONFIG_FILE)
        try:
            relative_file_path = configs[name]
        except Exception:
            raise KeyError(f'no setting for "{name}" in configs/{PATH_CONFIG_FILE}.yml')
        file_path = Path().home() / relative_file_path   
    else:
        files_in_path = EXAMPLE_PATH.glob(f'**/{name}*')
        file_path = list(files_in_path)[0]      
    if not file_path.exists():
        raise OSError(f'file not found:\n{file_path}')
    return file_path