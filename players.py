"""Player class and related functions."""


class Player:
    """Player class and related values."""

    def __init__(self, player_number, hand_size, endtile):
        """Initialize player pieces and util values."""
        self.player_number = player_number
        self.hand_size = hand_size
        self.tiles = []
        self.open = False
        self.possible_trains = [
            [[13, 13], [13, endtile]]
        ]

    def _find_useable_tiles(self, report):
        """Review at all trains that can be built on your own board."""
        useble_tiles = []
        for tile in self.tiles:
            if report[-1] in tile:
                useble_tiles.append(tile)
        return useble_tiles

    def build_train(self):
        """Append a useable tile to a theoretical train."""
        useble_tiles = self.report_my_tiles()
        for tile in useble_tiles:
            for train in self.possible_trains:
                if not train:
                    self.possible_trains.remove(None)
                    break
                self._align_tile(tile, train[-1][1])
                added: list = train.append(tile)
                self.possible_trains.append(added)
        return self.possible_trains

    def _align_tile(self, tile, end):
        """Rotate tile as necessay.

        Ex: tile = [2,1], end = 1
        returns [1,2]
        """
        if tile[0] != end:
            tile.reverse()
        return tile

    def report_my_tiles(self):
        useable_tiles = []
        for train in self.possible_trains:
            for tile in self.tiles:
                if train[-1][1] in tile and train[-1][1] not in useable_tiles:
                    useable_tiles.append(self._align_tile(tile, train[-1][1]))
        return useable_tiles

