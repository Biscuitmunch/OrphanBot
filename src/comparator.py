import cv2
import numpy as np

# Importing Mahjong Tiles
# Terminals
bamb1_img = cv2.imread('Tiles\\Bamboo\\one_big.png', cv2.IMREAD_UNCHANGED)
bamb9_img = cv2.imread('Tiles\\Bamboo\\nine_big.png', cv2.IMREAD_UNCHANGED)
dot1_img = cv2.imread('Tiles\\Dots\\one_big.png', cv2.IMREAD_UNCHANGED)
dot9_img = cv2.imread('Tiles\\Dots\\nine_big.png', cv2.IMREAD_UNCHANGED)
char1_img = cv2.imread('Tiles\\Characters\\one_big.png', cv2.IMREAD_UNCHANGED)
char9_img = cv2.imread('Tiles\\Characters\\nine_big.png', cv2.IMREAD_UNCHANGED)

# Winds
east_img = cv2.imread('Tiles\\Winds\\east_big.png', cv2.IMREAD_UNCHANGED)
south_img = cv2.imread('Tiles\\Winds\\south_big.png', cv2.IMREAD_UNCHANGED)
west_img = cv2.imread('Tiles\\Winds\\west_big.png', cv2.IMREAD_UNCHANGED)
north_img = cv2.imread('Tiles\\Winds\\north_big.png', cv2.IMREAD_UNCHANGED)

# Dragons
green_img = cv2.imread('Tiles\\Dragons\\green_big.png', cv2.IMREAD_UNCHANGED)
red_img = cv2.imread('Tiles\\Dragons\\red_big.png', cv2.IMREAD_UNCHANGED)
white_img = cv2.imread('Tiles\\Dragons\\white_big.png', cv2.IMREAD_UNCHANGED)

# Importing Mahjong Buttons
skip_img = cv2.imread('Buttons\\skip.png', cv2.IMREAD_UNCHANGED)
riichi_img = cv2.imread('Buttons\\riichi.png', cv2.IMREAD_UNCHANGED)
tsumo_img = cv2.imread('Buttons\\tsumo.png', cv2.IMREAD_UNCHANGED)
ron_img = cv2.imread('Buttons\\ron.png', cv2.IMREAD_UNCHANGED)

# Importing timer section of board
timer_img = cv2.imread('Board\\timer.png', cv2.IMREAD_UNCHANGED)

# Auto button section of board
auto_img = cv2.imread('Board\\auto_buttons.png', cv2.IMREAD_UNCHANGED)

def check_orphan_type(tile_position):
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

    yloc, xloc = np.where(one_bamb_match >= 0.95)
    for (x, y) in zip(xloc, yloc):
        return int(x), int(y), 1
    
    yloc, xloc = np.where(nine_bamb_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 2

    yloc, xloc = np.where(one_dot_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 3

    yloc, xloc = np.where(nine_dot_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 4

    yloc, xloc = np.where(one_char_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 5

    yloc, xloc = np.where(nine_char_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 6

    yloc, xloc = np.where(east_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 7

    yloc, xloc = np.where(south_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 8

    yloc, xloc = np.where(west_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 9

    yloc, xloc = np.where(north_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 10

    yloc, xloc = np.where(green_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 11

    yloc, xloc = np.where(red_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 12

    yloc, xloc = np.where(white_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 13

    return 0, 0, 0

def check_button_type(button_position):
    skip_match = cv2.matchTemplate(button_position, skip_img, cv2.TM_CCOEFF_NORMED)
    riichi_match = cv2.matchTemplate(button_position, riichi_img, cv2.TM_CCOEFF_NORMED)
    tsumo_match = cv2.matchTemplate(button_position, tsumo_img, cv2.TM_CCOEFF_NORMED)
    ron_match = cv2.matchTemplate(button_position, ron_img, cv2.TM_CCOEFF_NORMED)

    yloc, xloc = np.where(skip_match >= 0.95)
    for (x, y) in zip(xloc, yloc):
        return int(x), int(y), 'skip'
    
    yloc, xloc = np.where(riichi_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 'riichi'

    yloc, xloc = np.where(tsumo_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 'tsumo'

    yloc, xloc = np.where(ron_match >= 0.95)
    for (x,y) in zip(xloc, yloc):
        return int(x), int(y), 'ron'

def check_turn_timer(timer_position):
    timer_match = cv2.matchTemplate(timer_position, timer_img, cv2.TM_CCOEFF_NORMED)

    yloc, xloc = np.where(timer_match >= 0.95)
    for(x,y) in zip(xloc, yloc):
        print('false')
        return False

    print('true')
    return True

def check_round_status(auto_button_position):
    auto_button_match = cv2.matchTemplate(auto_button_position, auto_img, cv2.TM_CCOEFF_NORMED)

    yloc, xloc = np.where(auto_button_match >= 0.95)
    for(x,y) in zip(xloc, yloc):
        return True
    
    return False