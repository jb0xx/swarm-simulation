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

class Visualizer():
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


    # def fill_blocks(surface, grid, color=GRAY):
    #     for row in grid.grid:
    #         for block in row:
                

    #     rect = (0,0,10,10)    
    #     pygame.draw.rect(surface,color,rect)

    # def fill_block(surface, grid, x, y, w, h, color=GRAY):
        
    #     rect = (0,0,10,10)    
    #     pygame.draw.rect(surface,color,rect)
        