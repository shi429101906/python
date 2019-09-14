# 判断空白字符串
space_str = "     \t\n\r"

print(space_str.isspace())

# 判断字符串中是否只包含数字
# 1> 3个方法都不能判断小数
# num_str = '1.1'
# 2> unicode 字符串 isdigit isnumeric
# num_str = '\u00b2'
# 3> 中文数字 isnumeric
num_str = '一千零一'

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
