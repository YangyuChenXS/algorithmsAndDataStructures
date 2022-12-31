from threading import Thread
import threading

# 创建线程互斥锁
mutex = threading.Lock()
num = 0


def producer():
    global num
    times = 1000000
    while times >= 0:
        times -= 1
        mutex.acquire()
        num = num + 1
        mutex.release()
        print(num)


def consumer():
    global num
    times = 1000000
    while times >= 0:
        times -= 1
        mutex.acquire()
        num = num - 1
        mutex.release()
    print(num)


if __name__ == '__main__':
    producer_thread = Thread(target=producer, name='producer')
    consumer_thread = Thread(target=consumer, name='consumer')
    producer_thread.start()
    consumer_thread.start()


