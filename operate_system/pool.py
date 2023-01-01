import threading
from operate_system.task import Task
import pustil
from operate_system.queue import ThreadSafeQueue


# 任务处理线程
class ProcessThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, task_queue, *args, **kwargs)
        # 线程停止的标记
        self.dismiss_flag = threading.Event()
        # 任务队列(处理线程不断从队列取出元素)
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break

            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑（是通过函数调用引进来的）
            result = task.callable(*task.args, **task.kwargs)

    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()


# 线程池
class ThreadPool:
    def __init__(self, size=0):
        if not size:
            # 约定线程池的大小为CPU核数的两倍（最佳实践）
            size = psutil.cpu_count() * 2
            # 线程池
            self.pool = ThreadSafeQueue(size)
            # 任务队列
            self.task_queue = ThreadSafeQueue()

            for i in range(size):
                self.pool.put(ProcessThread(self.task_queue()))

    def start(self):
        pass

    def join(self):
        pass

    def put(self):
        pass

    def batch_put(self):
        pass

    def size(self):
        pass
