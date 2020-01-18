# 记录所有的名片字典
card_list = []

def show_menu():

    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():

    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1、提示用户输入名片的详细信息
    # pycharm 使用小技巧：若是想要修改一个变量的名称，但在代码中有许多个该变量，名称修改过于麻烦
    # 则可以将光标放在该变量名上，使用shift + F6，对变量名称进行重构，选择全部代码
    # 选择右键 ——> 重构 ——> 重命名
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入 QQ 号：")
    email_str = input("请输入邮箱：")

    # 2、使用用户输入的信息建立一个名片字典
    card_dict = {"name_str":name_str,
                 "phone_str":phone_str,
                 "qq_str":qq_str,
                 "email_str":email_str}

    # 3、将名片字典添加到列表中
    card_list.append(card_dict)

    # 4、提示用户添加成功
    print("添加 %s 的名片成功" % name_str)

def show_all():

    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录，请先使用新增功能添加名片")
        # return 可以返回一个函数的执行结果
        # 下方的代码不会被执行
        # 如果return 后边没有任何的内容，表示会返回到函数调用的位置，并且不返回任何的值
        return

    # 打印表头
    for name in ["姓名","电话","qq","邮箱"]:
        print(name,end="\t\t")

    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表一次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name_str"],card_dict["phone_str"],card_dict["qq_str"],card_dict["email_str"]))

def search_card():

    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1、提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2、遍历名片列表，查询要搜索的姓名，如果没有找着，需要提示用户
    for card_dict in card_list:
        if find_name == card_dict["name_str"]:

            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name_str"],
                                            card_dict["phone_str"],
                                            card_dict["qq_str"],
                                            card_dict["email_str"]))

            # TODO 针对找着的名片记录执行修改和删除的操作
            deal_card(card_dict)

            break

    else:
        print("抱歉没有找着 %s" % find_name)

def deal_card(find_dict):

    """处理查找到的名片
    :param find_dict: 查找到的名片
    """

    action_str = input("请选择要处理的操作 "
                       "[1]修改 [2]删除 [0]返回上级菜单：")

    if action_str == "1":

        find_dict["name_str"] = input_card_info(find_dict["name_str"],"想要修改姓名：")
        find_dict["phone_str"] = input_card_info(find_dict["phone_str"],"想要修改的电话：")
        find_dict["qq_str"] = input_card_info(find_dict["qq_str"],"想要修改的qq：")
        find_dict["email_str"] = input_card_info(find_dict["email_str"],"想要修改的邮箱号：")

        print("修改名片成功")

    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功")

def input_card_info(dict_value,tip_message):

    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 输入中的提示信息
    :return: 如果用户输入了值，就返回输入的值，否则返回兹迪纳中原有的值
    """
    # 1、提示用户输入内容
    result_str = input(tip_message)

    # 2、针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str

    # 3、如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value