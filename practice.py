# import random
# print(random.choice([1,3,5]))

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