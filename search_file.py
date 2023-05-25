# 查找文件
import os


# s = os.listdir('C:\\Users\\Administrator\\Desktop')
# print(s)
#
# key = input('请输入文件关键词：')
#
# for i in s:
#     if key in i:
#         print(i)
#     else:
#         pass
def findfile(key, inputdir='.'):
    found_list = []
    all_files = os.listdir(inputdir)
    for name in all_files:
        full_name = '.' + '/' + name
        if key in name:
            found_list.append(full_name)
        else:
            try:
                with open(full_name) as f:
                    for l in f:
                        if key in l:
                            found_list.append(full_name + ': ' + l.strip())
                            break
            except:
                pass
    return found_list


# 输入搜索关键字和路径
keyword = input('匹配关键字： ')
path = input('搜索目录(不填默认为当前目录)： ')
if not path.strip():
    path = '.'

result = findfile(keyword, path)

# 输出结果
print("=================匹配结果=================")
for r in result:
    print(r)
