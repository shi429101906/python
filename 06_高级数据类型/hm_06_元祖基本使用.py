info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1、取值和取索引
print(info_tuple[1])
# 已经知道数据的内容， 希望知道该数据在元祖中的索引
print(info_tuple.index(18))
# 2、统计技术
print(info_tuple.count('zhangsan'))
# 统计元祖中包含元素的个数
print(len(info_tuple))
