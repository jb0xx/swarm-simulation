import random

MAX_SPEED = 10
MAX_ACCEL = 4

class Position:
	def __init__(self, pos=None):
		self.x = None
		self.y = None


class Velocity:
	def __init__(self):
		self.x = 0
		self.y = 0


class BasicAgent:
	def __init__(self, pygame, agent_id, pos=None, vel=None):
		self.id = agent_id
		self.surface = pygame.display.get_surface()
		self.pos = Position()
		self.vel = Velocity()
		self.set_pos()
		self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

	def generate():
		self.set_pos()
		self.set_vel()


	def set_pos(self, pos=None):
		if pos is None:
			surf_width = self.surface.get_width()
			surf_height = self.surface.get_height()
			x = random.uniform(0,surf_width) 
			y = random.uniform(0,surf_height)
			self.pos.x = x
			self.pos.y = y
		else:
			self.pos.x = pos[0]
			self.pos.y = pos[1]


	def set_vel(self, vel=None):
		if vel is None:
			vx = random.uniform(-MAX_SPEED,MAX_SPEED) 
			vy = random.uniform(-MAX_SPEED,MAX_SPEED)
			self.vel.x = vx
			self.vel.y = vy
		else:
			self.vel.x = vel[0]
			self.vel.y = vel[1]


	def change_vel(self, dv=None):
		if dv is None:
			dv_x = random.gauss(0,MAX_ACCEL/4) 
			dv_y = random.gauss(0,MAX_ACCEL/4)
			dv = [dv_x, dv_y]
		self.vel.x += dv[0]
		self.vel.y += dv[1]
		self.vel.x = max(self.vel.x, -MAX_SPEED)
		self.vel.x = min(self.vel.x, MAX_SPEED)
		self.vel.y = max(self.vel.y, -MAX_SPEED)
		self.vel.y = min(self.vel.y, MAX_SPEED)
		

	def update(self):
		self.pos.x += self.vel.x
		self.pos.y += self.vel.y
		self.reflect_boundary()
		self.change_vel()


	def reflect_boundary(self):
		surf_width = self.surface.get_width()
		surf_height = self.surface.get_height()
		if self.pos.x > surf_width:
			self.pos.x = surf_width
			self.vel.x *= -1
		if self.pos.x < 0:
			self.pos.x = 0
			self.vel.x *= -1
		if self.pos.y > surf_height:
			self.pos.y = surf_height
			self.vel.y *= -1
		if self.pos.y < 0:
			self.pos.y = 0
			self.vel.y *= -1




	def rand_move(self):
		decision = random.random()





