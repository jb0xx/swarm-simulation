import numpy as np


WHITE = (255, 255, 255)

class Dimensions:
    x: float
    y: float



class Grid:
    def __init__(self, pygame, size=(12,8)):
        self.grid = [[[] for _ in range(size[0])] for _ in range(size[1])]
        self.block_dims = Dimensions()
        self.game = pygame
        self.surface = pygame.display.get_surface()
        self._set_bounds(size)


    def _set_bounds(self, grid_size, agents=None):
        (grid_size_x, grid_size_y) = grid_size
        self.block_dims.x = self.surface.get_width() / grid_size_x
        self.block_dims.y = self.surface.get_height() / grid_size_y


    def update_agent(self, agent):
        """ updates the agent's location on the grid """
        loc = self.convert_pos_to_loc(agent.pos)
        self.move_agent(agent, loc)


    def move_agent(self, agent, loc_new):
        """ moves the agent to the specified location on the board """
        if self.remove_agent(agent):
            self.add_agent(agent, loc_new)
        else:
            print(f"Agent {agent.id} could not be found the on board.")


    def add_agent(self, agent, loc=None):
        """ adds the agent to the board, assumes the agent is not already on the board """
        if loc is None:
            loc = self.convert_pos_to_loc(agent.pos)
        (loc_x, loc_y) = loc
        self.grid[loc_y][loc_x].append(agent)

    
    # def remove_agent(self, agent, loc=None, loc_guess=None, radius=1):
    def remove_agent(self, agent, loc=None):
        """ remove an agent from the grid, check loc if specified """
        if loc is not None:
            loc_x = loc[0]
            loc_y = loc[1]
            bucket = self.grid[loc_y][loc_x]
            if agent in bucket:
                bucket.remove(agent)
                return True
        else:
            for row in self.grid:
                for bucket in row:
                    if agent in bucket:
                        bucket.remove(agent)
                        return True
        return False


    def get_agents_in_region(self, bounds):
        agents = []
        for b in bounds:
            b = convert_pos_to_loc(b)
        (x_min, x_max, y_min, y_max) = bounds
        subgrid = self.grid[y_min:y_max+1][x_min:x_max+1]
        for row in subgrid:
            for bucket in row:
                agents += bucket
        return agents


    def get_occupied_locs(self):
        """ return the locations occupied by agents in the grid """
        locs_occupied = []
        for i in range(len(self.grid)):
            row = self.grid[i]
            for j in range(len(row)):
                if len(row[j]) > 0:
                    locs_occupied.append((j,i))
        return locs_occupied


    def convert_pos_to_loc(self, pos):
        """ converts a screen position into a grid location """
        loc_x = int(pos.x / self.block_dims.x)
        loc_y = int(pos.y / self.block_dims.y)
        return (loc_x, loc_y)


