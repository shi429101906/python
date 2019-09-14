"""
1、定义字符串变量 name, 输出 我的名字叫 小明，请多多关照！
2、定义证书变量 student_no, 输出 我的学号是 000001
3、定义小数 price、 weight、 money， 输出 苹果单价 9.00 元/斤， 购买了5.00斤，需要支付45.00元
4、定义小数scale, 输出数据比例是10.00%
"""
name = "小明"
print("我的名字叫 %s,请多多关照！" % name)
student_no = 1
print("我的学号是 %06d" % student_no)
price = 9
weight = 5.00
money = 45.00
print("苹果单价 %.2f 元/斤， 购买了 %.2f 斤， 需要支付 %.2f 元" % (price, weight, money))
scale = 10
print("输出数据比例是%.2f%%" % (scale * 10))
