from enum import Enum
import cv2
import numpy as np
import mss

# Importing Mahjong Tiles
# Terminals
bamb1_img = cv2.imread('Tiles\\Bamboo\\one.png', cv2.IMREAD_UNCHANGED)
bamb9_img = cv2.imread('Tiles\\Bamboo\\nine.png', cv2.IMREAD_UNCHANGED)
dot1_img = cv2.imread('Tiles\\Dots\\one.png', cv2.IMREAD_UNCHANGED)
dot9_img = cv2.imread('Tiles\\Dots\\nine.png', cv2.IMREAD_UNCHANGED)
char1_img = cv2.imread('Tiles\\Characters\\one.png', cv2.IMREAD_UNCHANGED)
char9_img = cv2.imread('Tiles\\Characters\\nine.png', cv2.IMREAD_UNCHANGED)

# Winds
east_img = cv2.imread('Tiles\\Winds\\east.png', cv2.IMREAD_UNCHANGED)
south_img = cv2.imread('Tiles\\Winds\\south.png', cv2.IMREAD_UNCHANGED)
west_img = cv2.imread('Tiles\\Winds\\west.png', cv2.IMREAD_UNCHANGED)
north_img = cv2.imread('Tiles\\Winds\\north.png', cv2.IMREAD_UNCHANGED)

# Dragons
green_img = cv2.imread('Tiles\\Dragons\\green.png', cv2.IMREAD_UNCHANGED)
red_img = cv2.imread('Tiles\\Dragons\\red.png', cv2.IMREAD_UNCHANGED)
white_img = cv2.imread('Tiles\\Dragons\\white.png', cv2.IMREAD_UNCHANGED)

# Importing Mahjong Buttons
skip_img = cv2.imread('Buttons\\skip.png', cv2.IMREAD_UNCHANGED)
riichi_img = cv2.imread('Buttons\\riichi.png', cv2.IMREAD_UNCHANGED)
tsumo_img = cv2.imread('Buttons\\tsumo.png', cv2.IMREAD_UNCHANGED)
ron_img = cv2.imread('Buttons\\ron.png', cv2.IMREAD_UNCHANGED)

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

def check_orphan(tile_position):

    one_bamb_match = cv2.matchTemplate(tile_position, bamb1_img, cv2.TM_CCOEFF_NORMED)
    nine_bamb_match = cv2.matchTemplate(tile_position, bamb9_img, cv2.TM_CCOEFF_NORMED)
    one_dot_match = cv2.matchTemplate(tile_position, dot1_img, cv2.TM_CCOEFF_NORMED)
    nine_dot_match = cv2.matchTemplate(tile_position, dot9_img, cv2.TM_CCOEFF_NORMED)
    one_char_match = cv2.matchTemplate(tile_position, char1_img, cv2.TM_CCOEFF_NORMED)
    nine_char_match = cv2.matchTemplate(tile_position, char9_img, cv2.TM_CCOEFF_NORMED)
    east_match = cv2.matchTemplate(tile_position, east_img, cv2.TM_CCOEFF_NORMED)
    south_match = cv2.matchTemplate(tile_position, south_img, cv2.TM_CCOEFF_NORMED)
    west_match = cv2.matchTemplate(tile_position, west_img, cv2.TM_CCOEFF_NORMED)
    north_match = cv2.matchTemplate(tile_position, north_img, cv2.TM_CCOEFF_NORMED)
    green_match = cv2.matchTemplate(tile_position, green_img, cv2.TM_CCOEFF_NORMED)
    red_match = cv2.matchTemplate(tile_position, red_img, cv2.TM_CCOEFF_NORMED)
    white_match = cv2.matchTemplate(tile_position, white_img, cv2.TM_CCOEFF_NORMED)

    