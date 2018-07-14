import pygame


DISP_WIDTH = 800
DISP_HEIGHT = 600
NUM_AGENTS = 100

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)


def draw_agent(surface, agent, color=None, radius=10):
    if color is None: color = agent.color
    pos = [int(agent.pos.x), int(agent.pos.y)]
    pygame.draw.circle(surface, color, pos, radius)


def draw_gridlines(surface, grid, color=WHITE):
    pos_x = 0
    pos_y = 0
    w = surface.get_width()
    h = surface.get_height()
    while pos_x < w:
        pos_x += grid.block_dims.x
        pygame.draw.line(surface, color, (pos_x,0), (pos_x,h))
    while pos_y < h:
        pos_y += grid.block_dims.y
        pygame.draw.line(surface, color, (0,pos_y), (w,pos_y))


def fill_occupied_blocks(surface, grid):
    locs = grid.get_occupied_locs()
    for loc in locs:
        fill_block(surface,grid,loc)


def fill_block(surface, grid, loc, color=GRAY):
    w = grid.block_dims.x
    h = grid.block_dims.y
    loc_x, loc_y = loc
    rect = (loc_x*w,loc_y*h,w,h)    
    pygame.draw.rect(surface,color,rect)
