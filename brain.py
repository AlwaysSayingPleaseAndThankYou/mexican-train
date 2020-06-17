"""Module for the problem solving parts of the player
"""


class Brain:
    """Class for seperating out problem solving logic
    Trying to reduce complexity of player class
    """
    def __init__(self, tiles):
        self.possible_trains = []
        self.tiles = tiles

    def find_useable_tiles(self, report):
        """Review all possible trains,
        return tiles that can be added to them.
        For Local use only - does not inspect other player trains."""
        useble_tiles = []
        for tile in self.tiles:
            if report[-1] in tile:
                useble_tiles.append(tile)
        return useble_tiles

    def build_train(self):
        """Append a useable tile to a theoretical train."""
        # TODO: need to remove possible train tile from tiles
        useble_tiles = self.report_my_tiles()
        for tile in useble_tiles:
            useble_tiles.remove(tile)
            for train in self.possible_trains:
                if tile[0] == train[-1][1] or tile[1] == train[-1][1]:
                    self._align_tile(tile, train[-1][1])
                    train.append(tile)
        return self.possible_trains

    def clean_trains(self):
        """Remove trains that are shorter than max length."""
        train_lens = []
        for train in self.possible_trains:
            train_lens.append(len(train))
        for train in self.possible_trains:
            if len(train) < max(train_lens):
                self.possible_trains.remove(train)
