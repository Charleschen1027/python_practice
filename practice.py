# import random
# print(random.choice([1,3,5]))
from typing import List

#函数的定义和调用
# def sayHello():
#     print("Hello world!")
#
# sayHello()

# 创建一个函数 func，有一个名为 param 的参数
# 在函数中，将输入参数的数值乘以2，作为返回值
# def func(param):
#     param*=2
#     return param
#
# p = func(20)
# print(p)
# 定义带参数的函数
# def sayHello(someone):
#     print(someone,'says Hello!')
#
# sayHello('Charles')


# 函数的返回值1
# def double(a):
#     return a * 2
#
# x = 3
# y = double(x)
# print(y)

# 给函数 hello 设定一个参数 name
# 如果没有提供 name 参数的值，默认使用 'world'
# def hello(name='world'):
#     print('hello ' + name)
#
#
# hello()
# hello('python')

# total = 0
#
#
# # 将 total 设定为全局变量，使其在函数中有效
#
# def add(x):
#     global total
#     total += x
#
#
# def multi(x):
#     global total
#     total *= x
#
#
# add(10)
# multi(3)
# print(total)

# 不指定参数数量,参数存储在元组中
# def printAll(*args):
#     for i in args:
#         print(i,end='')
#     print()
#
# printAll(1,2,3)
# printAll(3,2,1)

# 不指定参数数量，参数存储在字典中
# def printAll(**kargs):
#     for k in kargs:
#         print(k, ':', kargs[k])
#
#
# printAll(a=1, b=2, c=3)
# printAll(x=4, y=5)

#操作列表
# # 创建一个列表 lst，其中的元素依次是 1，2，3
# lst = [1, 2, 3]
#
# # 输出 lst 中的第一个元素 1
# print(lst[0])
#
# #将 lst 的第二个元素 2 改为 4
# lst[1] = 4
#
# # 在 lst 末尾再增加一个元素 5
# lst.append(5)
#
# print(lst)

# #列表切片
# lst = [365, 'everyday', 0.618, True, 2, 5]
#
# # 取出 lst 的第二个位置至倒数第二个位置的子列表
# # 赋值给新的列表 lst2
# lst2 = lst[1:-1]
# print(lst2)

# 字符串分割为列表
# a = 'i love python'
# l = a.split()
# print(l)

# split()带参数
# a = 'www.crossincode.com'
# l = a.split('.')
# print(l)

# list方法将字符串转换成列表
# a = 'crossin'
# l = list(a)
# print(l)
#
# b = ' '.join(l)
# print(b)

# 输出1-100中可以同时被2,3,5整除的整数
# 用;连接输出
# result: list[str] = []
# for i in range(1,100):
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         result.append(str(i))
#
# print(';'.join(result))

# lst1 = [1, 2, 3, 5, 8, 13, 22]
#
# # 将lst1中的每一项都乘以2，生成新的列表lst2
# # 建议用列表解析式实现
# lst2 = [i*2 for i in lst1]
# print(lst2)
#
# word = 'I am Mr Crossin of Python'
#
# # 将字符串 word 按照空格分割成一个列表
# lst = word.split(' ')
#
# # 再将分割后的列表 lst 以逗号(,)为连接字符重新拼接成字符串 word2
# word2 = ','.join(lst)
#
# print(word2)

# 创建一个字典，包含 one、two、three 三个键
# 对应的值分别为 1，2，3
# data = {
#     'one':1,
#     'two':2,
#     'three':3
# }
#
# # 将 two 键对应的值改为 4
# data['two'] = 4
#
# print(data)

# get_after 函数的输入参数是一个整数
# 返回值是这个数后面递增1的两个整数（如参数10，返回 11, 12）
# 提示：使用元组作为函数的返回值
# def get_after(n):
#     return n+1,n+2
#
# # 调用 get_after
# after = get_after(10)
#
# # 输出 after 的第二项值
# # 参考输出：12
# print(after[1])

# 有一个全部由字符串组成的列表 list_s，统计列表中每个单词出现的次数。
list_s = ['Beautiful', 'is', 'better', 'than', 'ugly', 'Explicit', 'is', 'better', 'than', 'implicit']

dic_s = {}
for s in list_s:
    if s not in dic_s:
        dic_s[s] = 1
    else:
        dic_s[s] += 1

print(dic_s)
