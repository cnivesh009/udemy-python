# Document  : 5 StringProperties.py
# Created on : 16-07-2019, 12:12:26 AM
# Author       : Nivesh-GC

# Udemy: Complete Python BootCamp

# String is immutable
from datetime import datetime
now = datetime.now()  # displays current datetime

first_name = 'Nivesh'
last_name = 'Chandola'
# name[0] = 'n'  this is not permitted

# concatenating string
print(last_name + ", " + first_name)
x = 'Hello World'

print(x.upper())

print("\n%s" % x.split())
print("\n")

print(x.lower())

# ****************************String format****************************

print('\n****************String format****************')
print('This is a string {}'.format("THAT IS INSERTED"))
print('\nWhat does {} {} {}{}'.format('''the''', 'fox', "say", '?'))
print('\nI am {0} {2} {3} {1}.'.format('''the''', 'fox', "quick", 'brown'))
print('\nI am {t} {h} {m} {a}.'.format(
    t='''the''', h='handsome', a="alive", m='man'))

# ****************************Float format****************************
print('\n****************Float format****************')
a = 100
b = 777
print(" a = %d" % a + "\t b = %d" % b)

result = a / b
print('1. The result is {}'.format(result))
print("2. The result is {r}".format(r=result))

# Float formating follows {value:width.precisionf}
print("\n   # NOTE: Float formating follows {value:width.precisionf}")
print("3. The result is {r:1.3f}".format(r=result) +
      "\t   # Note the difference between 3 and 4")
print("4. The result is {r:10.5f}".format(r=result))
print("5. The result is %.3f" % result)

# f string
print("\n *****************f strings*****************")
name = "Harsh"
age = 26
# print(f"Hola, mi nombre es{name}")

print(f'6. Hola, mi nombre es {name} and I am {age} years old.')

# ************Date Time Format************
print('\n', '************Date Time Format************')

# yyyy-mm-dd h:m
dt = datetime(2019, 7, 16, 7, 45)   # has to be in this format
print('1.', dt)

# yyyy-mm-dd h:m
print('2. {:%Y-%m-%d %H:%M}'.format(datetime(2019, 7, 16, 4, 5)))

# dd-mm-yyyy    h:m am/pm
date_time = now.strftime("%d-%m-%Y %I:%M:%S %p")
print('3.', date_time)

# yyyy-mm-dd    H:M:S
date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print('4.', date_time)
