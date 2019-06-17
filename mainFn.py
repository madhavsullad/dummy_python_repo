# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:20:23 2019

@author: Madhav
"""

print(__name__)
def main1():
	print('Hello World')
	otherfn()
	
def otherfn():
	print('This is another fn')
	
if __name__ == '__main__':
	main1()