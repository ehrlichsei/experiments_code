class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # 用户角色，可以是 'admin', 'manager', 'user' 等

    def authenticate(self):
        # 简化的权限认证过程
        # 实际中可以根据具体情况进行更复杂的认证逻辑
        if self.role == 'admin':
            print(f"管理员 '{self.username}' 认证成功")
        elif self.role == 'manager':
            print(f"经理 '{self.username}' 认证成功")
        elif self.role == 'user':
            print(f"普通用户 '{self.username}' 认证成功")
        else:
            print(f"未知角色 '{self.role}'，认证失败")


class Admin(User):
    def __init__(self, username):
        super().__init__(username, role='admin')

    def some_admin_method(self):
        print("管理员方法")


class Manager(User):
    def __init__(self, username):
        super().__init__(username, role='manager')

    def some_manager_method(self):
        print("经理方法")

class RegularUser(User):
    def __init__(self, username):
        super().__init__(username, role='user')

    def some_user_method(self):
        print("普通用户方法")


# 示例用法
if __name__ == "__main__":
    # 创建不同角色的用户对象
    admin = Admin("admin_user")
    manager = Manager("manager_user")
    user = RegularUser("regular_user")

    # 用户认证
    admin.authenticate()
    manager.authenticate()
    user.authenticate()

    # 示例：尝试使用不同角色的方法
    try:
        admin.some_admin_method()
    except AttributeError:
        print("管理员方法只能由管理员调用")

    try:
        manager.some_manager_method()
    except AttributeError:
        print("经理方法只能由经理调用")

    try:
        user.some_user_method()
    except AttributeError:
        print("普通用户方法只能由普通用户调用")
