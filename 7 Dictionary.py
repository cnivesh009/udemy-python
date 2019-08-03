# Date: 21.07.2019
# Udemy: Complete Python BootCamp
# Last Edited: 16.07.2019

# *************Dictionaries*************
# These are unordered mappings for storing objects
# {'key1' : 'value1', 'key2' : 'value2' }
# Dictionaries can't be sorted; use it when sorting is not a priority

print('*************Dictionaries*************')
my_dict1 = {'key1': 'value1', 'key2': 'value2'}
print(my_dict1)
print(my_dict1['key1'])
print(my_dict1['key2'])

print('*************lower to upper case*************')
my_dict2 = {'key1': ['a', 'b', 'C']}
print(my_dict2['key1'][1].upper())
print('*************upper case to lower*************')
print(my_dict2['key1'][2].lower())

print('*************Mapping*************')
my_dict3 = {'apple': 2.99, 'mango': 5.89}
print(my_dict3)
print(my_dict3['apple'])

print('*************Append my_dict3*************')
my_dict3['tomato'] = 9.87
print(my_dict3)

print('\n*************Dictionary Keys*************')
print(my_dict1.keys())
print(my_dict2.keys())
print(my_dict3.keys())

print('\n*************Dictionary Values*************')
print(my_dict1.values())
print(my_dict2.values())
print(my_dict3.values())

print('\n*************Dictionary Paring*************')
print(my_dict1.items())
print(my_dict2.items())
print(my_dict3.items())
print('\n')
