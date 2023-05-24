# 处理文件中的数据
f = open('scores.txt', encoding='utf-8')
lines = f.readlines()
f.close()

results = []
for line in lines:
    data = line.split()
    sum = 0
    score_list = data[1:]
    for score in score_list:
        sum += int(score)
    result = '%s\t:%d\n' % (data[0], sum)
    results.append(result)

# 保存至文件
output = open('result.txt', 'w', encoding='utf-8')
output.writelines(results)
output.close()
