class Sports:
    def __init__(self, name):
        self.name = name

class PingPong(Sports):
    def __init__(self, name):
        super().__init__(name)
        self.venues = LinkedList()

class Football(Sports):
    def __init__(self, name):
        super().__init__(name)
        self.venues = LinkedList()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

class Venue:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"Venue: {self.name}, Location: {self.location}"

class SportsManager:
    def __init__(self):
        self.sports = []

    def add_sport(self, sport):
        self.sports.append(sport)

    def process_all_venues(self):
        for sport in self.sports:
            print(f"Processing venues for {sport.name}")
            sport.venues.print_list()

if __name__ == "__main__":
    # 创建体育活动管理器
    manager = SportsManager()

    # 创建乒乓球和足球对象
    ping_pong = PingPong("Ping Pong")
    football = Football("Football")

    # 添加场馆到乒乓球和足球
    ping_pong.venues.append(Venue("Ping Pong Arena 1", "Location A"))
    ping_pong.venues.append(Venue("Ping Pong Arena 2", "Location B"))
    football.venues.append(Venue("Football Stadium 1", "Location C"))
    football.venues.append(Venue("Football Stadium 2", "Location D"))

    # 将乒乓球和足球添加到管理器
    manager.add_sport(ping_pong)
    manager.add_sport(football)

    # 处理和分析所有体育活动的场馆
    manager.process_all_venues()
