i = 1
while i <= 9:
    j = 1
    while j <= i:
        # end="" 表示输出结束后不换行
        # \t 可以在控制台输出一个制表符， 协助在输出文本时对齐
        print('%d * %d = %d' % (j, i, i * j), end="\t")
        j = j + 1

    print('')  # 这一行的目的就是增加换行
    i = i + 1
