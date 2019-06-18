# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:46:10 2019

@author: Madhav
"""

class student():
	def register(self, regno, name, std, sec):
		self.regno = regno
		self.name = name
		self.std = std
		self.sec = sec
		
	def info(self):
		print('RegNo.:', self.regno, '\nName:', self.name, '\nStandard:', self.std, '\nSection:', self.sec, '\n')
		
		
madhav = student()
madhav.register(75, 'Madhav', '10', 'C')
madhav.info()

rk = student()
rk.register(106, 'RK', '10', 'A')
rk.info()