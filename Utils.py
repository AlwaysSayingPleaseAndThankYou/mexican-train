"""Functions a bunch of modules want to use."""


def align_tile(self, tile, end):
    """Rotate tile as necessay.

    Ex: tile = [2,1], end = 1
    returns [1,2]
    """
    if tile[0] != end:
        tile.reverse()
    return tile
