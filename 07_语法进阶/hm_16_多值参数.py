def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
# atuple = (2, 4, 6) 直接传递元祖跟上面的不一样， 相当于元祖中又放了一个元祖
# demo(1, atuple, name="小明", age=18)
