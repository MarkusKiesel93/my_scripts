from src.base_cli import CliBase
from src.tracker.finances.debt_tracker import DebtTracker


class CliTrackDebt(CliBase):
    def __init__(self):
        self.parser_description = 'Track debts in data file per person'

    def execute(self, args):
        debt_tracker = DebtTracker()
        if args.add:
            debt_tracker.add()
        elif args.info:
            debt_tracker.info()
        elif args.list:
            debt_tracker.list(args.list[0])
        elif args.delete_last:
            debt_tracker.delete_last(args.delete_last)
        elif args.periodic_debt:
            debt_tracker.periodic_debt()
        else:
            debt_tracker.info()

    def create_parser(self, sub_parser):
        sub_parser.add_argument(
            '-a', '--add', action='store_true', help='add a new debt or payback to the database')
        sub_parser.add_argument(
            '-i', '--info', action='store_true', help='list the dept for all persons')
        sub_parser.add_argument(
            '-ls', '--list', nargs=1, metavar='person', help='list all the depts for one person')
        sub_parser.add_argument(
            '-pd', '--periodic_debt', action='store_true', help='add periodic debt from config file')
        sub_parser.add_argument(
            '-dl', '--delete_last', type=int, nargs='?', const=1, metavar='n', help='delete last n rows (default: 1)')
