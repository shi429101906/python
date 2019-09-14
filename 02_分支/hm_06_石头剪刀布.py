# 注意，在导入工具包时，应该将导入的语句，放在文件的顶部
# 因为这样方便下方的代码，在任何需要的时候，使用工具包中的文件
import random

player = int(input("请出拳:0石头，1剪刀，2布"))
computer = random.randint(0, 2)

print('玩家输入的是 %d, 电脑输入的是 %d' % (player, computer))

# if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
if ((player == 0 and computer == 1)
        or (player == 1 and computer == 2)
        or (player == 2 and computer == 0)):

    print("欧耶，电脑弱爆了")
elif player == computer:
    print("真是心有灵犀啊")
else:
    print("不服气，决战到天亮")