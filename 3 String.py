# Document  : 3 String.py
# Created on : 14-07-2019, 12:58:31 AM
# Author       : Nivesh-GC

# Udemy: Complete Python BootCamp

print('******Various forms of writing String*******\n')
print('1.   hello')
print("2.   hello")
print('3.   This is a string')
print("4.   This is also a string")
print("5.   I want to fly")
print('''6.   How do you do''')
print('7.   Hello \n     world')
print('8.   Hello \tworld')
d = 'I am hungry!!'
e = len('I am hungry!!')
print("9.   d =  %s" % d)
print("10.  Number of characters in var d (int): %d" % e)
print("11.  Number of characters in var d (float): %.2f" % e)
print("12.  %s" % d[0])
print("13.  %s" % d[-3])
print("14. d[0: ] -->  %s " % d[0:])
print("\n15. d[4:]  --> %s" % d[4:])
print("\n16. d[:4]  --> %s" % d[:4])    # 0<=string;        string<4

# space is a character at index 4;string d[3: index<9]
print("\n17. d[3:9] --> %s" % d[3:9])
print("\n18. d[4:-2] --> %s \n" % d[4:-2])
print("\n19. d[: :] --> %s \n" % d[::])

# str[start :stop :step_size]
print("\n20. d[0: 9: 2] --> %s \n" % d[0: 9:2])


# Reverse of a string
print("\n21. d[: : -1] --> %s \n" % d[:: -1])
