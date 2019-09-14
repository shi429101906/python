# 输入苹果的单价
price = input('苹果的单价：')
# 输入苹果的重量
weight = input('苹果的重量：')
# 计算支付的总金额
# 注意两个字符串之间不能用乘法,需要将输入的字符串转换成浮点数
price = float(price)
weight = float(weight)
money = price * weight

print(money)