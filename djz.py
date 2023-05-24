# 斗地主手牌发放
import random

puke = []
# 13张基础牌
f_list = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 加花色
for f in f_list:
    puke.append('♥' + f)
    puke.append('♠' + f)
    puke.append('♣' + f)
    puke.append('♦' + f)
puke.append('R_Joker')
puke.append('B_Joker')
# print(puke)
# 随机打乱列表
random.shuffle(puke)
# 设定玩家
wj1 = []
wj2 = []
wj3 = []
while len(puke) != 0:
    wj1.append(puke.pop())
    wj2.append(puke.pop())
    wj3.append(puke.pop())
print(wj1, wj2, wj3)
