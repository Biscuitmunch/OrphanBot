from enum import Enum
from time import sleep
import cv2
import pyautogui
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
        Tiles.bamb1: False,
        Tiles.bamb9: False,
        Tiles.dot9: False,
        Tiles.dot9: False,
        Tiles.char1: False,
        Tiles.char9: False,
        Tiles.east: False,
        Tiles.south: False,
        Tiles.west: False,
        Tiles.north: False,
        Tiles.green: False,
        Tiles.red: False,
        Tiles.white: False
    }
    return d

orphan_tiles = set_tiles
duplicate_obtained = False
turns_forced = 0

# Screenshotter
sct = mss.mss()

tiles_owned = [Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, Tiles.Nothing, 
                Tiles.Nothing]

def force_turn(tile_number):
    global turns_forced
    turns_forced += 1
    print(tiles_owned)
    print(tile_number)
    while(True):
        sleep(1)
        turn_timer_picture = np.array(sct.grab(areas.timer_area))
        if(comparator.check_turn_timer(turn_timer_picture)):
            discard_area = areas.tile_1.copy()
            discard_area['left'] += 95 * tile_number
            discard_tile(discard_area)
            break

def dupe_check():
    global duplicate_obtained

    tile_amounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for tile in tiles_owned:
        if tile != Tiles.Nothing:
            tile_amounts[tile.value-1] += 1

    for i in range(0, 13):
        if tile_amounts[i] > 1 and duplicate_obtained == False:
            duplicate_obtained = True
            tiles_left = tile_amounts[i] - 2
            if tiles_left > 0:
                for j in range(0, 13):
                    if tiles_owned[j] == Tiles(i+1):
                        force_turn(j)
                        tiles_left -= 1
                        sleep(1)
                        check_all_tiles()

                    if (tiles_left == 0):
                        break

        elif tile_amounts[i] > 1:
            tiles_left = tile_amounts[i] - 1
            if tiles_left > 0:
                for j in range(0, 13):
                    if tiles_owned[j] == Tiles(i+1):
                        force_turn(j)
                        tiles_left -= 1
                        sleep(1)
                        check_all_tiles()

                    if (tiles_left == 0):
                        break

def check_all_tiles():

    tile_area = areas.tile_1.copy()

    for i in range(0, 13):
        tile_check = np.array(sct.grab(tile_area))
        tile_result = comparator.check_orphan_type(tile_check)
        if Tiles(tile_result[2]) != Tiles.Nothing:
            tiles_owned[i] = Tiles(tile_result[2])
        tile_area['left'] += 95

def check_draw_tile():
    tile_check = np.array(sct.grab(areas.tile_14))
    tile_result = comparator.check_orphan_type(tile_check)
    print("TILE INFO " + str(tile_result))
    return Tiles(tile_result[2])

# Pass a copy into this
def discard_tile(tile_area):
    pyautogui.moveTo(tile_area['left'] + 40, tile_area['top'] + 65)
    pyautogui.click()
    pyautogui.moveTo(960, 540)

check_all_tiles()

dupe_check()

while (turns_forced != 0):
    print("REPEAT DUPE")
    turns_forced = 0
    duplicate_obtained = False
    dupe_check()

while(True):
    print("DUPES FINISHED")
    sleep(1)
    check_all_tiles()
    turn_timer_picture = np.array(sct.grab(areas.timer_area))
    if(comparator.check_turn_timer(turn_timer_picture)):
        sleep(1)
        print(tiles_owned)
        drawn_tile = check_draw_tile()
        print("DRAWN TILE: " + str(drawn_tile))
        if drawn_tile == Tiles.Nothing:
            discard_tile(areas.tile_14)

        elif drawn_tile in tiles_owned and duplicate_obtained == True:
            discard_tile(areas.tile_14)

        else:
            if duplicate_obtained == False:
                if drawn_tile in tiles_owned:
                    duplicate_obtained = True
            for i in range(0, 13):
                if tiles_owned[i] == Tiles.Nothing:
                    tile_area = areas.tile_1.copy()
                    tile_area['left'] += 95 * i
                    print(tile_area)
                    discard_tile(tile_area)
                    break
                    