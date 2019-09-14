#!/usr/bin/python3

import cards_tools

while True:

    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作: ")
    print("您选择的操作是:【%s】" % action_str)

    if action_str in ['1', '2', '3']:
        if action_str == '1':
            cards_tools.add_card()
        elif action_str == '2':
            cards_tools.show_all()
        elif action_str == '3':
            cards_tools.search_card()
    elif action_str == '0':
        break
    else:
        print("请输入的不正确， 请重新再试")
