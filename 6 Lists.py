# Document  : 6 Lists.py
# Created on : 16-07-2019, 07:04:56 PM
# Author       : Nivesh-GC

# Udemy: Complete Python BootCamp

# *************list*************
mylist_1 = ['one', 'two', 'three']
mylist_2 = ['4', "5", '''6''']
print("1. " + mylist_1[2] + " " + mylist_2[0])
print("2. ", mylist_1 + mylist_2)

# change an element in the mylist_2
mylist_2[0] = 'ALL CAPS'
print("3. ", mylist_1 + mylist_2)

mylist_1[-2] = 'ALL CAPS'
print("4. ", mylist_1 + mylist_2)

# append list; adds an element at the end of the mylist_1
mylist_1.append('four')
print("5. ", mylist_1 + mylist_2)

# pop element; pops element from the end of the list
popped = mylist_2.pop()
print("6. ", mylist_1 + mylist_2)

popped = mylist_1.pop(1)
print("7. ", mylist_1 + mylist_2)

# sorting
print('\n *********Sorting*********')
new_list = ['a', 'e', 'i', 'o', 'u', 'z', 'c']
num_list = [15, 10, 100, 1000, 101, 100]

print("\nUnsorted List: ")
print(new_list, "\t", num_list)

# .sort() does not return anything
new_list.sort()
num_list.sort()

print("\nSorted List: ")
print(new_list, '''\t''', num_list)
print([1, 'car', 3.14])
