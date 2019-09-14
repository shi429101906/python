hello_str = 'hello world'

# 判断是否以指定字符串开始
print(hello_str.startswith("Hello"))

# 判断是否以指定的字符串结束
print(hello_str.endswith('world'))

# 查找指定字符串
# index方法同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find('llo'))
# index方法如果指定的字符串不存在，会报错
# find方法如果指定的字符串不存在，会返回-1
print(hello_str.find('abc'))

# 替换字符串
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(hello_str.replace('world', 'python'))

print(hello_str)


