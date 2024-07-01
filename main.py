from task_manager.task_scheduler import TaskScheduler
from task_manager.my_task import ExampleTask

from find_similar_words.find_similar_words_func import find_similar_words

from questionare.questionnare import Questionnaire
from questionare.option import Option
from questionare.question import Question
from questionare.user import User

import logging 

def run_task_manager():
    # 配置日志记录
    logging.basicConfig(level=logging.INFO)
    
    # 创建调度器实例
    scheduler = TaskScheduler()
    
    # 创建任务并添加到调度器中
    task1 = ExampleTask('Task1', 'param1')
    task2 = ExampleTask('Task2', 'param2')
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    
    # 执行任务
    scheduler.run_tasks()

def run_find_similar_words():
    word_list = ["apple", "apply", "orange", "banana", "pineapple"]
    word = "appel"
    similar_words = find_similar_words(word, word_list)
    print(similar_words)

def run_questionare():
    # 创建选项
    option1 = Option("非常尊重", 5)
    option2 = Option("一般尊重", 3)
    option3 = Option("不尊重", 0)

    # 创建问题并添加选项
    question1 = Question("这个人是否尊重女性？", {
        option1.text: option1.score,
        option2.text: option2.score,
        option3.text: option3.score
    })

    # 创建问卷并添加问题
    questionnaire = Questionnaire("尊重女性评估问卷")
    questionnaire.add_question(question1)

    # 创建用户
    user = User("张三")

    # 用户回答问题
    question1.set_answer("非常尊重")

    # 用户完成问卷并计算总分
    score = user.complete_questionnaire(questionnaire)
    print(f"用户 {user.name} 的总分是: {score}")



if __name__ == '__main__':
    # run_task_manager()
    # run_find_similar_words()
    run_questionare()