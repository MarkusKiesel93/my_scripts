import importlib
import argparse
from pathlib import Path


CLIS_PACKAGE = 'cli_scripts.clis'
CLIS_PATH = Path(__file__).parent / CLIS_PACKAGE.replace('.', '/')


def create_run_clis():
    # load CLI scripts
    cli_scripts = {}
    for cli_file in CLIS_PATH.glob('**/*.py'):
        cli_name = cli_file.stem
        class_name = 'Cli' + ''.join([word.title() for word in cli_name.split('_')])
        cli_scripts[cli_name] = {'class_name': class_name, 'file_name': f'.{cli_name}'}

    # load Classes
    classes = {}
    for cli in cli_scripts.keys():
        class_to_import = getattr(importlib.import_module(
            cli_scripts[cli]['file_name'],
            package=CLIS_PACKAGE),
            cli_scripts[cli]['class_name'])
        classes[cli] = class_to_import()

    # create parser
    parser = argparse.ArgumentParser(prog='My Scripts', description='collection of useful CLI scripts')
    subparsers = parser.add_subparsers(title='My Scripts', dest='script_to_run')

    # add sub parsers
    for cli in classes.keys():
        sub_parser = subparsers.add_parser(cli, description=classes[cli].parser_description)
        classes[cli].create_parser(sub_parser)

    # run script
    args = parser.parse_args()
    if not args.script_to_run:
        print('no script selected')
    else:
        classes[args.script_to_run].execute(args)
