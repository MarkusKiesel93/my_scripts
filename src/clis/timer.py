from src.base_cli import CliBase
from src.utilitys.timer import Timer


class CliTimer(CliBase):
    def __init__(self):
        self.parser_description = 'Timer for min and sec'

    def execute(self, args):
        timer = Timer(args.min, args.sec)
        timer.start()

    def create_parser(self, sub_parser):
        sub_parser.add_argument('min', type=int, help='minutes to time')
        sub_parser.add_argument('sec', type=int, nargs='?', default=0, help='seconds to time')
