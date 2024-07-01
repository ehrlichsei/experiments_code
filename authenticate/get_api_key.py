import uuid  # 用于生成唯一的 API 密钥

class User:
    def __init__(self, username):
        self.username = username
        self.api_key = str(uuid.uuid4())  # 生成一个随机的 API 密钥

    def get_api_key(self):
        return self.api_key

    def regenerate_api_key(self):
        self.api_key = str(uuid.uuid4())  # 重新生成 API 密钥

# 创建示例用户
user1 = User("user1")
print(f"用户 {user1.username} 的 API 密钥是：{user1.get_api_key()}")

# 示例：用户重新生成 API 密钥
user1.regenerate_api_key()
print(f"用户 {user1.username} 的新 API 密钥是：{user1.get_api_key()}")
