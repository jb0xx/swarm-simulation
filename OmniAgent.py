import math
import numpy as np

import Agents



class OmniAgent(Agents.BasicAgent):
	def __init__(self, pygame, agent_id, grid, pos=None, vel=None):
		self.id = agent_id
		self.surface = pygame.display.get_surface()
		self.pos = Position()
		self.vel = Velocity()
		self.set_pos()
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
