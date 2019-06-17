# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:25:47 2019

@author: Madhav
"""

lst = [2,4,1,47,38]
m = lst[0]
for num in lst[1:]:
	if num < m:
		m = num
		
print('Minimum = ', m)