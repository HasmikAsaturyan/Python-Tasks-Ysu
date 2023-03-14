# 1.
# import sys
# print(sys.version)

# 2.
# import datetime
# print(datetime.datetime.now())

# 3.
# from math import pi
# r = int(input('Enter the number: '))
# print(f'S = {pi*r**2}')

#4.
# filename = input('Enter the filrname: ')
# a = filename.split('.')
# print(a[-1])

#5.
# color_list = ["Red","Green","White","Black"]
# print(color_list[0],color_list[-1])

#6.
# exam_st_date = (11, 12, 2014)
# print(str(exam_st_date).replace(',','/'))

# 7.
# n = int(input('Enter the num: '))
# s = 0
# for i in range(1, n + 1):
#     s += n * i
# print(s)

# 8.
# n = int(input('Enter the num: '))
# if n % 2 == 0:
#     print('even')
# else:
#     print('zuyg')


# 9.
# mylist = [1, 5, 8, 3]
# n = int(input('Enter thr num: '))
# for i in mylist:
#     if n in mylist:
#         print('true')
#     else:
#         print('false')

# 10.
# def histrogram(nums):
#     for i in nums:
#         s = ''
#         while i > 0:
#             s += '#'
#             i-= 1
#         print(s)
# histrogram([2, 3, 6, 5])

#11.
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# for i in color_list_1:
#     if i in color_list_2:
#         continue
#     else:
#         print(i)

# 12.

# l = [1,2,4,5]
 
# res = " ".join([str(i) for i in l])
# print(res)



# 13.
# def func(a,b):
#     if a < b :
#         for i in range(a , 0 , -1):
#             if a % i == 0 and b % i == 0:
#                 return i
#     elif b < a :
#         for j in range(b , 0 , -1):
#             if b % i == 0 and a % i == 0 :
#                 return i 
#     else:
#         return 1
# print(func(int(input('Enter the number1: ')),int(input('Enter the number2: '))))

# 14.
# def func(a,b):
#     if a > b:
#         for i in range(a, a*b+1, a):
#             if i % b == 0:
#                 print(i)
#                 break
#     elif b > a:
#         for i in range(b, a*b+1, b):
#             if i % a == 0:
#                 print(i)
#                 break
# func(int(input('Enter the number1: ')),int(input('Enter the number2: ')))

#15
# def distance(x1,y1,x2,y2):
#     return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
# print(distance(3,4,5,6))

#16
# from os.path import exists

# file_exists = exists('homeworkuni.py')
# print(file_exists)

# 17.
# import struct
# print(struct.calcsize("P") * 8)

# 18.
# import platform
# import os
# print("Name of the operating system:",os.name)
# print("\nName of the OS system:",platform.system())
# print("\nVersion of the operating system:",platform.release())

#19.
# import subprocess
# import sys

# result = subprocess.run([sys.executable, "-c", "print('ocean')"])

# 20.
# import multiprocessing
# print(multiprocessing.cpu_count())

# 21.
# import os
# print(os.listdir())

# 22.
# x = int(input('Enter the num: '))
# y = int(input('Enter the num: '))
# z = int(input('Enter the num: '))

# a1 = min(x,y,z)
# a3 = max(x,y,z)
# a2 = (x + y + z)- a1 - a3
# print(a1,a2,a3)

# 23.?

# 24.?

# 25.
# def func(listt):
#     for i in listt:
#         a = listt.count(5)
#     return a
# print(func([5,6,7,8,2,4,3,2,6,8,9,9,5,5,2,]))

#26


# 27
# mylist = [1,2,3,4]
# mylist.pop(0)
# print(mylist)

# 28
# try:
#     a = int(input('Enter the number: '))

# except ValueError:
#     print('this is not a number')

# 29
# x = round(5.76543, 2)
# print(x)

# 30
# x = 'Hello python'
# print(any(i.islower() for i in x))

# 31

# 32
# import os.path
# print(os.path.expanduser('~'))

# 33
# print(int(True))
# print(int(False))

# 34
# x = 12
# print(format(x, '08b'))

# 35
# def min_max(mylist):
#     l = mylist[0]
#     s = mylist[0]

#     for i in mylist:
#         if i > l:
#             l = i
#         elif i < s:
#             s = i
#     return l,s
# print(min_max([2,3,4,5,6,7,8]))

# 36

# def func(x):
#     s = 0
#     for i in range(x):
#         s += i**3
#     return s
# print(func(8))
