"""Board with all the tile ends.

On the player turn, player consumes and updates the board.
"""
import random


class Board:
    """Class and related values to board."""

    def __init__(self, num_players, trick=12, turn=0):
        """Store possible boneyard values, mexican_train, and double lock."""
        self.trick = trick
        self.turn = turn
        self.boneyard = self._make_tiles()
        self.double = False
        self.mexican_train = trick
        self.boneyard.remove([trick, trick])
        # num_players + 1 to account for mexican train
        # Last value is always the mexican train
        self.opens = [False] * (num_players + 1)
        self.ends = [trick] * (num_players + 1)

    def _make_tiles(self):
        """Generate all possible tiles, [0,0]=>[12,12]."""
        tiles = []
        for j in range(13):
            for i in range(13):
                tiles.append([j, i])
        return tiles

    def report_playables(self):
        """Return end value for open trains"""
        playables = []
        for val in enumerate(self.opens):
            if val[1] is True:
                playables.append(self.ends[val[0]])
        return playables

    def play_tile(self, tile, player_num):
        """Take a tile from player, add it to the board"""
        # TODO: this can replace add_to_mexican_train
        # TODO: this necessitates a play_tile func for player to produce tile
        # - make it part of the turn function
        pass

    def deal_tile(self):
        """Give a tile out to a player, remove it from the boneyard."""
        index = random.choice(range(len(self.boneyard)))
        return self.boneyard.pop(index)

    def add_to_mexican_train(self, tile):
        """Add player tile to mexican train"""
        # TODO: tile should be sanitized and checked
        self.mexican_train.append(tile)
