class Resource:
    def __init__(self, name, resource_type):
        self.name = name
        self.resource_type = resource_type

class Permission:
    def __init__(self, name, action, resource=None):
        self.name = name
        self.action = action  # 允许的动作，如 "read", "write", "delete"
        self.resource = resource  # 关联的资源对象
    
    def has_access(self, user):
        # 检查用户是否有权限执行指定动作
        if self.resource:
            # 这里可以根据用户的角色或订阅方案来判断权限
            if user.has_permission(self):
                return True
            else:
                return False
        else:
            return False
        
# 示例用户类
class User:
    def __init__(self, username):
        self.username = username
        self.permissions = []

    def add_permission(self, permission):
        self.permissions.append(permission)

    def has_permission(self, permission):
        return permission in self.permissions

# 创建资源实例
book_resource = Resource("Book", "Library")
movie_resource = Resource("Movie", "Streaming")

# 创建权限实例
read_book_permission = Permission("Read Book", "read", book_resource)
write_book_permission = Permission("Write Book", "write", book_resource)
watch_movie_permission = Permission("Watch Movie", "read", movie_resource)


# 创建示例用户和权限
user1 = User("user1")
user1.add_permission(read_book_permission)
user1.add_permission(write_book_permission)
user1.add_permission(watch_movie_permission)

# 检查权限
print(read_book_permission.has_access(user1))  # True
print(write_book_permission.has_access(user1))  # True
print(watch_movie_permission.has_access(user1))  # True

def check_permission(user, action, resource):
    # 根据用户的权限列表进行验证
    for permission in user.permissions:
        if permission.action == action and permission.resource == resource:
            return True
    return False

# 示例：检查用户是否可以写入书籍资源
book_resource = Resource("Book", "Library")
if check_permission(user1, "write", book_resource):
    print("User has write access to Book resource.")
else:
    print("User does not have write access to Book resource.")
