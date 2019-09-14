result = 0

i = 0

while i <= 100:
    # 偶数 i % 2 == 0
    # 奇数 i % 2 != 0
    if i % 2 == 0:
        result += i
    i += 1

print('0~100的偶数累加结果是 %d' % result)
