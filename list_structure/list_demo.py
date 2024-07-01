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
            print(f"Name: {current_node.data.name}, Age: {current_node.data.age}")
            current_node = current_node.next

    def find(self, name):
        current_node = self.head
        while current_node:
            if current_node.data.name == name:
                return current_node.data
            current_node = current_node.next
        return None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age



if __name__ == "__main__":
    # 创建链表
    students = LinkedList()

    students.print_list()

    # 添加学生对象
    students.append(Student("Alice", 20))
    students.append(Student("Bob", 22))
    students.append(Student("Charlie", 23))

    # 打印学生对象
    students.print_list()

    # 添加新学生
    students.append(Student("David", 21))

    # 查找特定学生
    found_student = students.find("Alice")
    if found_student:
        print(f"Found Alice, Age: {found_student.age}")
    else:
        print("Alice not found")
