import uuid


# 基本任务对象
class Task:

    def __init__(self, func, *args, **kwargs):
        # 任务具体逻辑，通过函数引用传递进来
        self.callable = func
        self.id = uuid.uuid4()
        # 函数的参数
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return 'Task id: ' + str(self.id)


def my_function(self):
    print('this is a task test.')


if __name__ == '__main__':
    task = Task(func=my_function)
    print(task)