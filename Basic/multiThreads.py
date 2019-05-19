# 线程分为内核线程和用户线程
#   内核线程：由操作系统内核创建和撤销
#   用户线程：不需要内核支持而在用户程序中实现的线程

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)


def print_time(self, threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1


thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(1, "Thread-2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")


# 线程同步，Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法
# 对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间
# 当线程想要访问共享数据时，必须获得锁，否则需要等待其它线程释放锁，称为同步阻塞

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s : %s" % (threadName, time.ctime(time.time())))
        counter -=1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")


# 线程优先级队列
# Python的 Queue模块中提供了同步的、线程安全的队列类

import queue
import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()

