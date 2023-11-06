from cli_scripts.base_cli import CliBase
from cli_scripts.tracker.health.food_tracker import FoodTracker


class CliTrackFood(CliBase):
    def __init__(self):
        self.parser_description = 'Track food after feeling unwell'

    def execute(self, args):
        food_tracker = FoodTracker()
        food_tracker.track()