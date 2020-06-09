"""Class and related functions to the mexican train board."""
import random


class Board:
    """Class and related values to board."""

    def __init__(self, round=12, turn=0):
        """Store possible boneyard values, mexican_train, and double lock."""
        self.round = round
        self.turn = turn
        self.boneyard = self._make_tiles()
        self.double = False
        self.mexican_train = round
        self.boneyard.remove([round, round])

    def _make_tiles(self):
        """Generate all possible tiles, [0,0]=>[12,12]."""
        tiles = []
        for j in range(13):
            for i in range(13):
                tiles.append([j, i])
        return tiles

    def deal_tile(self):
        """Give a tile out to a player, remove it from the boneyard."""
        index = random.choice(range(len(self.boneyard)))
        return self.boneyard.pop(index)
