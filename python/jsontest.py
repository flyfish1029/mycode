#!/usr/bin/python3

import json

data={
        'no':1,
        'name':'Runoob',
        'url':'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python原始数据:", repr(data))
print("JSON对象:", json_str)
