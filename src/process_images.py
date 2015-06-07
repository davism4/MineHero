import pygame
import resources as res
import constants as con

def resize(sheet, (width, height), alpha=False):
    sheet = sheet.convert()
    new_sheet = pygame.Surface((width, height))
    pygame.transform.scale(sheet, (width, height), new_sheet)
    return new_sheet

# Basically, just enter the width and height of the image
# so far these are multiples of tile sizes, but some
# images (surfaces) may be other sizes:
def process():
    res.wall = resize(res.wall, (4*con.TILE_WIDTH, 4*con.TILE_WIDTH))
    res.stoneSheet = resize(res.stoneSheet, (4*con.TILE_WIDTH, 7*con.TILE_WIDTH))
    res.jones = resize(res.jones, (4*con.TILE_WIDTH, 4*con.TILE_WIDTH),True)
    return
