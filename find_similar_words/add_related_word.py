class Word:
    def __init__(self, word):
        self.word = word
        self.related_words = []

    def add_related_word(self, related_word):
        if related_word not in self.related_words:
            self.related_words.append(related_word)
            related_word.add_related_word(self)  # 同时在相关单词中添加反向关系

    def remove_related_word(self, related_word):
        if related_word in self.related_words:
            self.related_words.remove(related_word)
            related_word.remove_related_word(self)  # 同时在相关单词中移除反向关系
        else:
            print(f"单词 '{related_word.word}' 不在相关单词列表中。")

    def list_related_words(self):
        print(f"单词 '{self.word}' 的相关单词：")
        for related_word in self.related_words:
            print(related_word.word)

# 示例用法
if __name__ == "__main__":
    # 创建单词对象
    apple = Word("apple")
    fruit = Word("fruit")
    red = Word("red")
    juicy = Word("juicy")

    # 添加相关单词
    apple.add_related_word(fruit)
    apple.add_related_word(red)
    apple.add_related_word(juicy)

    fruit.add_related_word(apple)
    fruit.add_related_word(Word("banana"))  # 另一个单词对象

    # 打印相关单词
    apple.list_related_words()
    print()
    fruit.list_related_words()

    # 移除相关单词
    apple.remove_related_word(red)
    apple.list_related_words()

    fruit.remove_related_word(Word("banana"))
    fruit.list_related_words()
