"""Player class and related functions."""


class Player:
    """Player class and related values."""

    def __init__(self, player_number, hand_size, board):
        """Initialize player pieces and util values."""
        # TODO: must recompute train after getting doubled
        self.player_number = player_number
        self.hand_size = hand_size
        self.tiles = []
        self.open = False
        self.possible_trains = [
            [[13, 13], [13, board.round]]
        ]
        self.train = [[13, 13],[13, board.round]]
        self._create_player(board)

    def _create_player(self, board):
        """Deals tiles to player from board."""
        i = 0
        while i <= self.hand_size:
            self.tiles.append(board.deal_tile())
            i += 1

    def _find_useable_tiles(self, report):
        """Review at all trains that can be built on your own board."""
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

    def _align_tile(self, tile, end):
        """Rotate tile as necessay.

        Ex: tile = [2,1], end = 1
        returns [1,2]
        """
        if tile[0] != end:
            tile.reverse()
        return tile

    def report_my_tiles(self):
        """Find tiles that can be added to a train."""
        useable_tiles = []
        for train in self.possible_trains:
            for tile in self.tiles:
                if train[-1][1] in tile and train[-1][1] not in useable_tiles:
                    useable_tiles.append(self._align_tile(tile, train[-1][1]))
        return useable_tiles

    def clean_trains(self):
        """Remove trains that are shorter than max length."""
        train_lens = []
        for train in self.possible_trains:
          train_lens.append(len(train))
        for train in self.possible_trains:
            if len(train) < max(train_lens):
                self.possible_trains.remove(train)

    def take_turn(self, board):
        """Check doubles, mexican train or play tiles"""
        # TODO: Okay this needs to be tested
        # check if doubles on board
        if board.double:
            double_tile = board.mexican_train[-1][1]
            if [double_tile, double_tile] in self.tiles:
                self.tiles.remove([double_tile, double_tile])
                board.mexican_train.append([double_tile, double_tile])
                board.double = False
                # TODO: this must rebuild the theory train
        # play on my own train
        elif len(self.possible_trains) > 0:
            for tile in self.possible_trains:
                self.possible_trains.remove(tile)
                if tile not in self.train:
                    self.train.append(tile)
        # play on mexican train
        # TODO: This needs to go after doubles
        # TODO: this needs to check the other open trains as well
        elif len(self.tiles) > 0:
            final_tile = board.mexican_train[-1][1]
            for tile in self.tiles:
                if final_tile in tile:
                    self.tiles.remove(tile)
                    board.mexican_train.append(tile)
        # if this all fucks up draw
        else:
            self.tiles.append(board.deal_tile())

    def last_tile(self):
        # use this: https://stackoverflow.com/questions/6190468/how-to-trigger-function-on-value-change
        pass

