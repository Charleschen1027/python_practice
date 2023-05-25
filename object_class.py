# 面向对象

# class MyClass:
#     name = 'Sam'
#     def sayHi(self):
#         print('Hello %s' % self.name)
#
# mc = MyClass()
# print(mc.name)
# mc.name = 'Lily'
# mc.sayHi()

# 创建类 MyClass
class MyClass:
    # 创建属性 name，值为 Sam
    name = 'Sam'

    # 创建方法 sayHi
    def sayHi(self):
        print('Hello %s' % self.name)


# 创建一个 MyClass 的对象
mc = MyClass()

# 输出 mc 的 name 属性
print(mc.name)

# 调用 mc 的 sayHi 方法
mc.sayHi()
