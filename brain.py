"""Module for the problem solving parts of the player
"""


class Brain:
    """Class for seperating out problem solving logic
    Trying to reduce complexity of player class
    """
    def __init__(self, tiles):
        self.possible_trains = []
        self.tiles = tiles

