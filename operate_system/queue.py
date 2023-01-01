import threading
import time


class ThreadSafeQueueException(Exception):
    pass


# 线程安全的队列
class ThreadSafeQueue(object):

    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size
        self.lock = threading.Lock()
        # 同步条件和互斥锁应该同时使用，但是Python同步条件的逻辑已经包含了互斥锁，所以不需要额外再加锁
        self.condition = threading.Condition()

    # 当前队列元素的数量
    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    # 往队列里面放入元素
    def put(self, item):
        if self.max_size != 0 and self.size() > self.max_size:
            return ThreadSafeQueueException()
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()  # 通知阻塞等待的进程，可以不需要等待了
        self.condition.release()

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    # 从队列取出元素
    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            # 需要阻塞等待
            if block:
                self.condition.acquire()
                # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                # 表示需要等待的时间，如果在这个等待时间的过程内，收到了通知，则不再继续等待
                # 如果超过了等待时间，则也不等待
                self.condition.wait(timeout=timeout)
                # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                self.condition.release()
            else:
                return None
        if self.size() == 0:  # 有可能等待结束后，size还是0，所以需要一个判断
            return None
        self.lock.acquire()
        item = self.queue.pop()
        self.lock.release()
        return item

    def get(self, index):
        return self.queue[index]


if __name__ == '__main__':
    queue =  ThreadSafeQueue(max_size=100)

    def producer():
        while True:
            queue.put(1)
            time.sleep(8)

    def consumer():
        while True:
            item = queue.pop(block=True, timeout=3)
            print(item)
            time.sleep(1)

    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=consumer)
    thread1.start()
    thread2.start()
    thread1.join()  # 等待线程结束
    thread2.join()