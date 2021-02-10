from src.base_cli import CliBase
from src.tracker.finances.expense_tracker import ExpenseTracker


class CliTrackExpense(CliBase):
    def __init__(self):
        self.parser_description = 'Track my expanses in data file'

    def execute(self, args):
        expense_tracker = ExpenseTracker()
        if args.list:
            expense_tracker.list(args.list)
        elif args.add:
            expense_tracker.add()
        elif args.delete_last:
            expense_tracker.delete_last(args.delete_last)
        else:
            expense_tracker.list()

    def create_parser(self, sub_parser):
        sub_parser.add_argument(
            '-a', '--add', action='store_true', help='add a new expense to the database')
        sub_parser.add_argument(
            '-ls', '--list', type=int, nargs='?', const=10, metavar='n', help='list the last n rows (default: 10)')
        sub_parser.add_argument(
            '-dl', '--delete_last', type=int, nargs='?', const=1, metavar='n', help='delete last n rows (default: 1)')
