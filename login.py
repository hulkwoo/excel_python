from person import Person
import os
from excel import Excel
import test

print("欢迎使用人员信息管理系统！")

# 用于模拟当前的用户信息
users_data = []
users_data.append(Person("张三", "123456"))
users_data.append(Person("李四", "123456"))
users_data.append(Person("王五", "123456"))
users_data.append(Person("赵六", "123456"))
users_data.append(Person("老七", "123456"))


# 用于登陆操作
def login():
    login_name = input("请输入用户名：")
    login_pwd = input("请输入密码：")
    if login_name != "admin" and login_pwd != "admin":
        pass
    else:
         start_person_system()


# 用于查看用户信息
def find_users_info():
    print("编号\t用户名\t密码")
    i = 1
    for user in users_data:
        print("{0}\t{1}\t\t{2}".format(i, user.name, user.pwd))
        i += 1


# 通过当前的用户的编号查询当前用户的数据
def get_user_by_no(index=int):
    if index > len(users_data):
        return None
    else:
        return users_data[index]


def update_user_info():
    no = input("请输入需要修改的用户的编号：")
    if int(no) - 1 > len(users_data):
        print("当前的用户编号不存在，请检查输入！")
    else:
        choose = input("是否修改当前 {0} 的数据信息？(y/Y)".format(get_user_by_no(int(no) - 1).name))
        if choose.lower() == "y":
            update_name = input("请输入修改后的用户名称：")
            update_pwd = input("请输入修改后的用户的密码：")
            users_data[int(no) - 1] = Person(update_name, update_pwd)
            print("修改用户信息成功！")


# 添加用户信息
def add_user_info():
    add_name = input("请输入需要添加的用户的名称：")
    add_pwd = input("请输入需要添加的用户的密码：")
    users_data.append(Person(add_name, add_pwd))
    print("添加用户信息成功！")


# 通过当前用户的编号删除当前用户的信息
def delete_user_info_by_no():
    del_no = input("请输入需要删除用户的编号：")
    if int(del_no) - 1 > len(users_data):
        print("当前用户编号不存在！")
    else:
        choose = input("是否刪除当前 {0} 的数据信息？(y/Y)".format(get_user_by_no(int(del_no) - 1).name))
        if choose.lower() == "y":
            del_user = users_data.pop(int(del_no) - 1)
            print("当前删除的用户的信息为：用户名：{0}，密码：{1}".format(del_user.name, del_user.pwd))



#表格操作
file_path = os.getcwd() + '/data.xlsx'
excel = Excel(file_path)


# 登录后的操作界面
def start_person_system():
    while True:
        user_input = input("输入当前需要操作的编号!输入q或者Q退出)\n1.查询sheet\t2.修改\t3.添加用户信息\t4.删除用户的信息\n")
        if user_input == "1":
            find_users_info()
        elif user_input == "2":
            update_user_info()
        elif user_input == "3":
            add_user_info()
        elif user_input == "4":
            delete_user_info_by_no()
        elif user_input == "5":
            add_excel()
        elif user_input == "6":
            list = excel.read_all_sheetnames(file_path)
            print('sheet names：\n',list)
        elif user_input == "7":
            while True:
                list = []
                user_input = input("输入查询表名称：")
                for i in range
                list =excel.read_sheet_data()
        else:
            if user_input.lower() == "q":
                print("感谢使用本系统！您已退出！")
                break
        
        

login()
