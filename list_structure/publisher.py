class NewsPublisher:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, news_type, subscriber):
        if news_type not in self.subscribers:
            self.subscribers[news_type] = []
        self.subscribers[news_type].append(subscriber)

    def unsubscribe(self, news_type, subscriber):
        if news_type in self.subscribers:
            self.subscribers[news_type].remove(subscriber)

    def publish(self, news_type, news):
        if news_type in self.subscribers:
            for subscriber in self.subscribers[news_type]:
                subscriber.receive_news(news_type, news)


class Student:
    def __init__(self, name):
        self.name = name

    def receive_news(self, news_type, news):
        print(f"{self.name} received {news_type} news: {news}")


# 示例使用
news_publisher = NewsPublisher()

student1 = Student("Alice")
student2 = Student("Bob")

# 学生订阅新闻
news_publisher.subscribe("Sports", student1)
news_publisher.subscribe("Sports", student2)
news_publisher.subscribe("Technology", student1)

# 发布新闻
news_publisher.publish("Sports", "Team A won the championship!")
news_publisher.publish("Technology", "New breakthrough in AI research!")

# 学生取消订阅
news_publisher.unsubscribe("Sports", student2)

# 发布更多新闻
news_publisher.publish("Sports", "Player X set a new record!")
news_publisher.publish("Technology", "Quantum computing is the future!")
