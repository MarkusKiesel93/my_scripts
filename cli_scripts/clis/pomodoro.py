from cli_scripts.base_cli import CliBase
from cli_scripts.timer import Timer


class CliPomodoro(CliBase):
    def __init__(self):
        self.parser_description = 'Pomodoro for productive working'

    def execute(self, args):
        pomodoro = Timer(args.min_pomo, output='POMODORO')
        short_break = Timer(args.short_break, output='SHORT BREAK')
        long_break = Timer(args.long_break, output='LONG BREAK')

        while True:
            pomodoro.start()
            short_break.start()
            pomodoro.start()
            long_break.start()

            if not args.loop:
                break

    def create_parser(self, sub_parser):
        sub_parser.add_argument('min_pomo', type=int, nargs='?', default=25, help='minutes for pomodoro')
        sub_parser.add_argument('short_break', type=int, nargs='?', default=5, help='minutes for short break')
        sub_parser.add_argument('long_break', type=int, nargs='?', default=15, help='minutes for long break')
        sub_parser.add_argument('-lo', '--loop', action='store_true')
