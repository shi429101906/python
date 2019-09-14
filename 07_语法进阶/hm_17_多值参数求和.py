def sum_numbers(*args):
# def sum_numbers(args):

    num = 0
    for arg in args:
        num += arg

    return num


sums = sum_numbers(1, 2, 3, 4, 5, 6, 7, 8)
# sums = sum_numbers((1, 2, 3, 4, 5, 6, 7, 8))
print(sums)
