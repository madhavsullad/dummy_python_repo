# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:37:41 2019

@author: Madhav
"""

lst = [2,4,1,47,38]

def summ():
	ans = 0
	for num in lst:
		ans += num
	print('Answer = ', ans)
	
def maxx():
	m = lst[0]
	for num in lst:
		if num > m:
			m = num
			
	print('Maximum = ', m)
	
def minn():
	m = lst[0]
	for num in lst:
		if num < m:
			m = num
			
	print('Minimum = ', m)
	
def avg():
	avg = 0

	for num in lst:
		avg += num
	
	print('Average = ', avg/len(lst))
	
def search():
	flag = 0
	key = int(input('Enter the number to search:'))

	for num in lst:
		if key == num:
			print('Found in the list!')
			flag = 1
			break
	if flag == 0:
		print('Not found!')
	

summ()
maxx()
minn()
avg()
search()