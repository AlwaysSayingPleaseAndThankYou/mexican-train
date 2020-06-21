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
        self.spare_tiles = []
        self.train = [[13, 13], [13, board.trick]]
        self._create_player(board)

    def _create_player(self, board):
        """Deals tiles to player from board."""
        i = 0
        while i <= self.hand_size:
            self.tiles.append(board.deal_tile())
            i += 1

    def play_tile(self, board, tile, target):
        """Receives a tile to play from Brain function.

        This is where tiles are finally removed from the game.
        Target is index of train to play on - it is not cheeked here.
        """
        # TODO: This needs to use board.play_tile
        board.play_tile(tile, target, self.player_number)
        self.tiles.remove(tile)
        self.workingTrain.remove(tile)

    def draw_tile(self, board):
        """Draw a tile if you can't play.
        Handles it if there's not tile left to draw."""
        if len(board.boneyard) == 0:
            print('cant draw')
        else:
            self.tiles.append(board.deal_tile())

    def last_tile(self):
        # use this: https://stackoverflow.com/questions/6190468/how-to-trigger-function-on-value-change
        if len(self.tiles) == 1:
            print('tap tap')

    def take_turn(self, board):
        # TODO: when do I rebuild working_train after someone plays on my train?
        """
        1. Get report from board
        2. Play on own train if open
        2. Play on report if possible
        3. Play on own train if not
        4. Draw if you can't play
        5. Tap tile.
        """
        pass
