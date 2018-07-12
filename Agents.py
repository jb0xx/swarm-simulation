import random

MAX_SPEED = 10
MAX_ACCEL = 4


class Position:
	x: int
	y: int



class Velocity:
	def __init__(self):
		self.x = 0
		self.y = 0



class BasicAgent:
	def __init__(self, pygame, grid, agent_id, color=None, pos=None, vel=None):
		self.id = agent_id
		self.surface = pygame.display.get_surface()
		self.pos = Position()
		self.vel = Velocity()
		self.color = BasicAgent.rand_color() if color is None else color
		self.grid = grid
		self.set_pos()


	def set_pos(self, pos=None):
		if pos is None:
			surf_width = self.surface.get_width()
			surf_height = self.surface.get_height()
			self.pos.x = random.uniform(0,surf_width)
			self.pos.y = random.uniform(0,surf_height)
		else:
			(self.pos.x, self.pos.y) = pos
	

	def set_vel(self, vel=None):
		if vel is None:
			vx = random.uniform(-MAX_SPEED,MAX_SPEED) 
			vy = random.uniform(-MAX_SPEED,MAX_SPEED)
			self.vel.x = vx
			self.vel.y = vy
		else:
			self.vel.x = vel[0]
			self.vel.y = vel[1]


	def rand_color():
		return (random.randint(0,255), random.randint(0,255), random.randint(0,255))


	def change_vel(self, dv=None):
		if dv is None:
			dv = [random.gauss(0,MAX_ACCEL/4), random.gauss(0,MAX_ACCEL/4)]
		temp_vel_x = self.vel.x + dv[0]
		temp_vel_y = self.vel.y + dv[1]
		self.vel.x = min(max(temp_vel_x, -MAX_SPEED), MAX_SPEED)
		self.vel.y = min(max(temp_vel_y, -MAX_SPEED), MAX_SPEED)
		

	def update_trajectory(self):
		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
		self.reflect_boundary()
		self.change_vel()


	def reflect_boundary(self):
		surf_width = self.surface.get_width()
		surf_height = self.surface.get_height()
		if self.pos.x >= surf_width:
			self.pos.x = surf_width-1
			self.vel.x *= -1
		if self.pos.x < 0:
			self.pos.x = 0
			self.vel.x *= -1
		if self.pos.y >= surf_height:
			self.pos.y = surf_height-1
			self.vel.y *= -1
		if self.pos.y < 0:
			self.pos.y = 0
			self.vel.y *= -1








