import pygame
import time

import Agents
from Draw import Visualizer as V
import Grid


DISP_WIDTH = 800
DISP_HEIGHT = 600
NUM_AGENTS = 10
BLACK = (0, 0, 0)

running = True

# clock = pygame.time.Clock()
def main():
    global running
    grid, agents = initialize_environment()

    surface = pygame.display.get_surface()
    while running:
        propagate_game(grid, agents)
    pygame.quit()
    quit()


def propagate_game(grid, agents):
    surface = pygame.display.get_surface()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print(event)
    surface.fill(BLACK)
    V.draw_gridlines(surface,grid)
    # V.fill_block(surface,grid)
    update_agents(surface,agents)
    pygame.display.update()


def update_agents(surface, agents):
    for a in agents:
        update_agent(surface,a)


def update_agent(surface, agent):
    agent.update_trajectory()
    agent.grid.update_agent(agent)
    V.draw_agent(surface,agent)


def initialize_environment(caption = 'Colliding Drones', disp_w = DISP_WIDTH, disp_h = DISP_HEIGHT):
    pygame.init()
    surface = pygame.display.set_mode((disp_w,disp_h))
    pygame.display.set_caption(caption)
    grid = initialize_grid(surface)
    agents = initialize_agents(grid)
    return grid, agents


def initialize_grid(surface, field_ratio=40):
    w = surface.get_width()
    h = surface.get_height()
    grid_size = (int(w/field_ratio), int(h/field_ratio))
    grid = Grid.Grid(pygame, size=grid_size)
    return grid


def initialize_agents(grid, num_agents=NUM_AGENTS):
    agents = []
    for i in range(num_agents):
        agent = Agents.BasicAgent(pygame,grid,i)
        agents.append(agent)
        grid.add_agent(agent)
    return agents


if __name__ == '__main__':
    tic = time.clock()
    main()
    toc = time.clock()
    print(f'time elapsed: {toc - tic}')
