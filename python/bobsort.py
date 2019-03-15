#!/usr/bin/python3
#-*- coding:utf-8 -*-
import random

def listproductor(lengthl, minnum, maxnum):
    i = 0
    testl = []
    while i < lengthl-1 :
        tmp = random.randint(minnum, maxnum)
        testl.append(tmp)
        i += 1
        
    return testl

#testlist = [1,2,5,9,7,6,8]
testlist=listproductor(10, 10, 50)
print(testlist) 

def bobsort(lists):
	b=0
	a=b
	while b <= len(testlist) and a < len(testlist):
		while a < len(testlist)-b-1:
			if testlist[a] > testlist[a+1]:
				testlist[a],testlist[a+1] = testlist[a+1],testlist[a]
			a += 1
			print(testlist)
		b += 1
		a = 0
	return lists

testlist2=bobsort(testlist)
print(testlist2)
