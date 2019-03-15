#!/usr/bin/python3
import re

phone = "2004-959-599#这是一个电话号码"
#删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码:", num)

#移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码:", num)
