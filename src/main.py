from enum import Enum
from time import sleep
import cv2
import numpy as np
import mss
import comparator
import areas

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

tiles_owned = [Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing]

def check_all_tiles():

    tile_area = areas.tile_1.copy()
    print(areas.tile_1['left'])

    for i in range(0, 13):
        tile_check = np.array(sct.grab(tile_area))
        tile_result = comparator.check_orphan_type(tile_check)
        if tile_result[2] != Tiles.Nothing:
            tiles_owned[i] = tile_result[2]
        tile_area['left'] += 95


while(True):
    sleep(5)
    check_all_tiles()
    print(tiles_owned)