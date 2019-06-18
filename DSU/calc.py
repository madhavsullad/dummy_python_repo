# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:56:18 2019

@author: Madhav
"""

class calc():
	def add(self, a, b):
		return (a+b)
	
	def sub(self, a, b):
		return (a-b)
	
	def mul(self, a, b):
		return (a*b)
	
	def div(self, a, b):
		if b!=0:
			return (a/b)
		else:
			print('\nCannot divide by Zero!\n')
	
calculator = calc()
print('Sum = ', calculator.add(9,10))

print('Difference = ', calculator.sub(9,10))

print('Product = ', calculator.mul(9,10))

print('Division = ', calculator.div(9,2))