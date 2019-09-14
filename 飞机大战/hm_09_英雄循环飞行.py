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

# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(190, 650, 100, 124)

# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 可以指定循环体内部代码的执行频率
    clock.tick(60)

    # 判断飞机的位置
    if hero_rect.y <= -124:
        hero_rect.y = 852

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4. 调用update方法更新显示
    pygame.display.update()


pygame.quit()
