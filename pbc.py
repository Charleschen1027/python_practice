# 屏蔽词替换
import jieba


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        global lines
        lines = [l.strip() for l in f.readlines()]  # 去掉换行符后保存

    # return lines


def fenci(s):
    s = ''.join(jieba.cut(s))
    return s


content = input("请输入内容：")
content_c = fenci(content)

read_file('pbc_l.txt')
for x in lines:
    content_c = content_c.replace(x, '*' * len(x))
print(content_c)
