card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def add_card():
    print("-" * 50)
    print("新增名片")
    name = input('请输入姓名：')
    phone = input('请输入电话：')
    qq = input('请输入qq：')
    email = input('请输入邮箱：')
    card_dict = {"name": name, "phone": phone, "qq": qq, "email": email}
    card_list.append(card_dict)
    print('添加 %s 名片成功' % name)


def show_all():
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) <= 0:
        print("当前没有任何的名片记录， 请使用新增功能添加名片")
        return

    print("姓名\t\t电话\t\tqq\t\t邮箱")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))


def search_card():
    print("-" * 50)
    print("搜索名片")
    action_str = input("请输入要搜索的姓名: ")
    for card_dict in card_list:
        if action_str == card_dict['name']:
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))
            deal_card(card_dict)
            break
    else:
        print("抱歉， 没有找到 %s" % action_str)


def deal_card(card_dict):

    action_str = input("请选择要执行的操作 【1】修改 【2】删除 【0】返回上级菜单")
    if action_str == '1':
        card_dict['name'] = input_by_card("姓名：", card_dict['name'])
        card_dict['phone'] = input_by_card("电话：", card_dict['phone'])
        card_dict['qq'] = input_by_card("qq：", card_dict['qq'])
        card_dict['email'] = input_by_card("邮箱：", card_dict['email'])
        print("修改成功")

    elif action_str == '2':
        card_list.remove(card_dict)
        print("删除成功")


def input_by_card(tips, dict_value):
    return_str = input(tips)
    if len(return_str) <= 0:
        return dict_value
    else:
        return return_str
