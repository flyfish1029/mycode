#!/usr/bin/python3
#-*- encoding:utf-8 -*-

def fibolaqi(length):
    i=0
    a=0
    b=1
    tl=[]
    while i < length:
        c = a+b
        tl.append(b)
        a = b
        b = c
        i += 1

    return tl

print(fibolaqi(20))
