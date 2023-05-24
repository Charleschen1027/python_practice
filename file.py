# 写入文件
# txt = ['Hello~\n','How are you?\n','Fine.Thank you. And you?']
#
# with open('out.txt','w') as f:
#     f.writelines(txt)

# 处理异常
# try:
#     f = open('non-exist.txt')
#     print('File opened!')
#     f.close()
# except:
#     print('File not exists.')
# print('Done')
# 为以下代码增加异常处理，使其运行结束
# try:
#     a = int('0.5')
#     print(a)
# except:
#     #发生异常时输出
#     print('error: convert "0.5" to int')
#
# print('Done')

# 编码解码
s = '你好'
print(s.encode('utf8'))
print(s.encode('gbk'))

b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b.decode())
print(b.decode('gbk'))
