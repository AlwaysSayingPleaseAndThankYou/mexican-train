"""Player class and related functions."""


class Player:
    """Player class and related values."""

    def __init__(self, player_number, hand_size, endtile):
        """Initialize player pieces and util values."""
        self.player_number = player_number
        self.hand_size = hand_size
        self.tiles = []
        self.open = False
        self.train = [[13, endtile]]
        self._possible_trains = [
            [[13, 13], [13, endtile]]
        ]

    def _find_useable_tiles(self, report):
        """Review at all trains that can be built on your own board."""
        useble_tiles = []
        for tile in self.tiles:
            if report[-1] in tile:
                useble_tiles.append(tile)
        return useble_tiles

    def build_train(self, useble_tiles):
        """Append a useable tile to a theoretical train."""
        print('this is build_train')
        while(len(useble_tiles) > 0):
            tile = useble_tiles.pop()
            print('this is the tile were working with')
            print(tile)
            for train in self._possible_trains:
                if not train:
                    continue
                print('this is the train')
                print(train)
                if train[-1][1] in tile:
                    tile_to_place = self._align_tile(tile, train[-1][1])
                    self._possible_trains.append(train.append(tile_to_place))
                    print('finishing the a loop')
        return self._possible_trains

    def _align_tile(self, tile, end):
        """Rotate tile as necessay.

        Ex: tile = [2,1], end = 1
        returns [1,2]
        """
        if tile[0] != end:
            tile.reverse()
        return tile
