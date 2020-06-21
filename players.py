"""Player class and related functions."""
from Utils import align_tile


class Player:
    """Player class and related values."""

    def __init__(self, player_number, hand_size, board):
        """Initialize player pieces and util values."""
        # TODO: must recompute train after getting doubled
        self.player_number = player_number
        self.hand_size = hand_size
        self.tiles = []
        self.open = False
        self.workingTrain = []
        self.train = [[13, 13], [13, board.round]]
        self._create_player(board)

    def _create_player(self, board):
        """Deals tiles to player from board."""
        i = 0
        while i <= self.hand_size:
            self.tiles.append(board.deal_tile())
            i += 1

    def last_tile(self):
        # use this: https://stackoverflow.com/questions/6190468/how-to-trigger-function-on-value-change
        pass

