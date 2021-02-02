# Base CLI class to define functions every CLI needs to implement


class CliBase:
    def __init__(self):
        self.parser_description = 'example decription for the parser'

    def execute(self, args):
        pass

    def create_parser(self, sub_parser):
        pass
