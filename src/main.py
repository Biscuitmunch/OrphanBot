from enum import Enum
import cv2
import comparator
import numpy as np
import mss

# Tile values
class Tiles(Enum) :
    Nothing=0
    bamb1=1
    bamb9=2
    dot1=3
    dot9=4
    char1=5
    char9=6
    east=7
    south=8
    west=9
    north=10
    green=11
    red=12
    white=13

# Tile storage
def set_tiles():
    d = {
        'bamb1': False,
        'bamb9': False,
        'dot1': False,
        'dot9': False,
        'char1': False,
        'char9': False,
        'east': False,
        'south': False,
        'west': False,
        'north': False,
        'green': False,
        'red': False,
        'white': False
    }
    return d

orphan_tiles = set_tiles
duplicate_orphan = Tiles.Nothing

# Screenshotter
sct = mss.mss()

tile_positions = [[312, 938], [407, 938], [502, 938], [597, 938], 
                [692, 938], [787, 938], [882, 938], [977, 938], [1072, 938], 
                [1167, 938], [1262, 938], [1357, 938], [1452, 938], [1575, 938]]