def print_line(char, times):
    """打印单行分割线
    :param char:
    :param times:
    :return:
    """
    print(char * times)


def print_lines(char, times):
    """打印分割线
    :param char:
    :param times:
    :return:
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines('a', 10)
