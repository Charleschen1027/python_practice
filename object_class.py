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
# class MyClass:
#     # 创建属性 name，值为 Sam
#     name = 'Sam'
#
#     # 创建方法 sayHi
#     def sayHi(self):
#         print('Hello %s' % self.name)
#
#
# # 创建一个 MyClass 的对象
# mc = MyClass()
#
# # 输出 mc 的 name 属性
# print(mc.name)
#
# # 调用 mc 的 sayHi 方法
# mc.sayHi()

# class Car:
#     speed = 0
#     def drive(self, distance):
#         time = distance / self.speed
#         print(time)
#
# car = Car()
# car.speed = 60.0
# car.drive(100.0)
#
# car2 = Car()
# car2.speed = 150.0
# car2.drive(100.0)
# car2.drive(200.0)

# 继承
class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print('花费 %f 小时' % (distance / self.speed))


class Bike(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, speed, fuel):
        Vehicle.__init__(self, speed)
        self.fuel = fuel

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print('消耗 %f 升油' % (distance * self.fuel))


b = Bike(15.0)
# b.speed = 15.0
c = Car(80.0, 0.012)
b.drive(100.0)
c.drive(100.0)
