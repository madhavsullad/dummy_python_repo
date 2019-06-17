# -*- coding: utf-8 -*-
class car:
	def __init__(self, make, model, color, price):
		self.make = make
		self.model = model
		self.color = color
		self.price = price
		
	def start(self):
		self.speed = 0
	
	def move(self):
		self.speed += 5
		
	def stop(self):
		self.speed = 0
		
	def info(self):
		print('\nMake:', self.make, '\nModel:', self.model, '\nColor:', self.color, '\nPrice:', self.price, '\nSpeed:', self.speed, '\n')
		
	
spyder = car('Porche', '911-Spyder', 'Black', 2300000)
		
spyder.start()
spyder.move()
spyder.move()
spyder.move()
spyder.move()
spyder.info()
spyder.stop()
spyder.info()
