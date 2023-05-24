import random

# 输入玩家名字
name = input("请输入你的名字：")

# #读取游戏结果
# f = open('game.txt')
# score = f.read().split()
# f.close()

with open('game2.txt') as f:
    lines = f.readlines()
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]  # 第一项为key,剩下的作为value
score = scores.get(name)  # 找到当前玩家的数据

if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0

print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (name, game_times, min_times, avg_times))

num = random.randint(1, 100)
times = 0  # 记录本局游戏轮数
print("Guess what I think?")
bingo = False
while bingo == False:
    times += 1
    answer = int(input())
    if answer < num:
        print("Too small!")
    elif answer > num:
        print("Too big!")
    else:
        print("bingo!")
        bingo = True

if game_times == 0 or times < min_times:
    min_times = times

total_times += times
game_times += 1

# 把成绩更新到对应的玩家数据中
# 加str转成字符串，为后面的格式化做准备
scores[name] = [str(game_times), str(min_times), str(total_times)]
result = ''  # 初始化一个空字符串，用来存储数据

for n in scores:
    line = n + ' ' + ' '.join(scores[n]) + '\n'
    result += line

with open('game2.txt', 'w') as f:
    f.write(result)
