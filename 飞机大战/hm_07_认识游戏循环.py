import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口 480 * 852
screen = pygame.display.set_mode((480, 852))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()


# 绘制英雄的飞机
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero, (190, 650))

# 可以在所有绘制工作完成之后， 统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

i = 0
# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 可以指定循环体内部代码的执行频率
    clock.tick(1)
    print(i)
    i += 1

pygame.quit()
