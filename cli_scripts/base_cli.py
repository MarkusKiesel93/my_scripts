# Base CLI class to define functions every CLI needs to implement
# Naming convention for all CLIs has to hold
# Name class with "Cli" and first letter upper case of module name


class CliBase:
    def __init__(self):
        self.parser_description = 'example decription for the parser'

    def execute(self, args):
        pass

    def create_parser(self, sub_parser):
        pass
