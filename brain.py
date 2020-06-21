"""Module for the problem solving parts of the player
"""


def align_tile(tile, end):
    """Rotate tile as necessay.

    Ex: tile = [2,1], end = 1
    returns [1,2]
    """
    if tile[0] != end:
        tile.reverse()
    return tile


class Brain:
    """Class for seperating out problem solving logic
    Trying to reduce complexity of player class

    This is a 3 step processs repeated until no more tiles can be placed

    1. find useable

    2. build train

    3. clean

    At the end it returns a extras pile and train that's being worked towards
    This process runs at game start and after every double is resolved

    The values of possible trains and tiles shadow the values Player has.
    Brain cannot directly affect those values, merely copies of them.
    It will the return tiles that should be played by the player.
    """
    def __init__(self, tiles):
        self.possible_trains = []
        self.tiles = tiles

    def _report_train_ends(self):
        """Generate ends of possible trains
        Makes train_ends for find_useable_tiles"""
        report = []
        for train in enumerate(self.possible_trains):
            for tile in self.tiles:
                if tile[0] in train[1][-1] or tile[1] in train[-1][1]:
                    report.append(tile)
        return report

    def find_useable_tiles(self, trains):
        # pass board.trains to this for general use
        # pass self.possible trains for internal use
        """Review all available trains,
        return tiles that can be added to them.

        This function is also useful for evaluating existing board states
        In this case, report comes from Board.report playables
        """
        # TODO: what do we do to catch no useable tiles
        train_ends = [train[-1] for train in trains]
        useble_tiles = []
        for tile in self.tiles:
            for train in train_ends:
                if train[1] in tile:
                    useble_tiles.append(tile)
                    self.tiles.remove(tile)
        return useble_tiles

    def build_train(self):
        """Append a useable tile to a theoretical train."""
        # TODO: need to remove possible train tile from tiles
        # TODO: Okay, i'm gonna rework this
        train_ends = self._report_train_ends()
        useable_tiles = self.find_useable_tiles(self.possible_trains)
        for tile in useable_tiles:
            useable_tiles.remove(tile)
            for train in self.possible_trains:
                if tile[0] == train[-1][1] or tile[1] == train[-1][1]:
                    align_tile(tile, train[-1][1])
                    train.append(tile)
        return self.possible_trains

    def clean_trains(self):
        """Remove trains that are shorter than max length."""
        # TODO: this has to put unused tiles back into the tile pool
        train_lens = []
        for train in self.possible_trains:
            train_lens.append(len(train))
        for train in self.possible_trains:
            if len(train) < max(train_lens):
                self.possible_trains.remove(train)
