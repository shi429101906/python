def sum_numbers(num):

    print(num)
    # 递归的出口， 当参数满足某个条件时， 不再执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_numbers(num - 1)

    print("完成了 %d" % num)


sum_numbers(3)

