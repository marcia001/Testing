#!/usr/bin/python

dict12 = {'name':'feifei', 'age':36, 'company':'baidu'}

for each in dict12.keys():
    print(each)

for each in dict12.values():
    print(each)

for each in dict12.items():
    print(each)

print(list(dict12.keys()))
print(list(dict12.values()))

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(dict))

dict1 = {1:'baidu', 2:'sina', 3:'google'}
print(dict1.setdefault(2))
print(dict1.setdefault(6))
print(dict1.setdefault(7,'美团'))
print(dict1)
