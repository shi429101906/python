class Tool(object):

    # 使用赋值语句定义类属性, 记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.count += 1


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 知道使用 Tool 类到底创建了多少个对象？
print("现在创建了 %d 个工具" % Tool.count)
