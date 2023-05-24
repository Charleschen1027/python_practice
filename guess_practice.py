# 在教程最开始的几课里，有一个猜数字的游戏：程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，直到猜中为止。
#
# 现在，请你独立实现这个小游戏，并且加上一些功能，比如：
# 游戏可以反复进行，猜中了之后可以重新开始
# 统计用户猜了几轮，平均几次猜中
# 1.程序随机结果
import random
rounds = 0  # 统计总轮次
counts = 0  # 统计猜对轮次
flag = 1  # 标志位，控制重新开始游戏
while flag == 1:
    rounds += 1  # 总轮次+1
    right_num = random.randint(1, 100)
    # 2.获取用户输入
    while True:
        input_num = int(input("请输入数字："))
        counts += 1  # 次数+1
        # 3.猜数字过程
        if input_num > right_num:
            print("哈哈，猜大了！")
        elif input_num < right_num:
            print("哈哈，猜小了！")
        else:
            print("恭喜你,猜对了!")

            flag = int(input("如需重新开始游戏，请输入1，否则输入0\n"))
            break
# 4.统计结果
print(f"总共进行了{rounds}轮")
print(f"平均{counts/rounds}次猜中")
