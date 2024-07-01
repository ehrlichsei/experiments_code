class TranslationMethod:
    def __init__(self, name):
        self.name = name

    def translate(self, text):
        raise NotImplementedError("Subclasses should implement this method")


class BasicTranslation(TranslationMethod):
    def __init__(self):
        super().__init__("Basic Translation")

    def translate(self, text):
        return f"[Basic Translation] Translating '{text}'..."


class AdvancedTranslation(TranslationMethod):
    def __init__(self):
        super().__init__("Advanced Translation")

    def translate(self, text):
        return f"[Advanced Translation] Translating '{text}' with advanced algorithms..."


class TranslationMachine:
    def __init__(self, access_level):
        self.access_level = access_level
        self.translation_methods = {
            "basic": BasicTranslation(),
            "advanced": AdvancedTranslation()
        }

    def translate(self, text, method):
        if method in self.translation_methods:
            translation_method = self.translation_methods[method]
            # Check access level before using the translation method
            if self.check_access(method):
                return translation_method.translate(text)
            else:
                return f"Access denied for translation method '{method}'"
        else:
            return f"Translation method '{method}' not found"

    def check_access(self, method):
        # Example: Access level check
        if method == "advanced" and self.access_level == "admin":
            return True
        elif method == "basic":
            return True
        else:
            return False


# 示例用法
if __name__ == "__main__":
    machine = TranslationMachine(access_level="admin")

    # 使用基础翻译
    result_basic = machine.translate("Hello", method="basic")
    print(result_basic)

    # 使用高级翻译（需要管理员权限）
    result_advanced = machine.translate("Hello", method="advanced")
    print(result_advanced)

    # 普通用户权限只能使用基础翻译
    user_machine = TranslationMachine(access_level="user")
    result_user = user_machine.translate("Hello", method="advanced")
    print(result_user)

    result_user2 = user_machine.translate("Hello", method="basic")
    print(result_user2)

