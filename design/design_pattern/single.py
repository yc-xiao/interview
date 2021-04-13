"""
    单例模式: 只有一个实例(全局对象)
    使用场景:
        1. 频繁实例化，再消耗的对象，减少资源开销。
        2. 全局管理对象，用于生成唯一值
"""
import threading
import time

class SingleNoLock():
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            time.sleep(0.01)
            cls._instance = super(SingleNoLock, cls).__new__(cls)
        return cls._instance

class Single:
    _lock = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kw):
        """
            1. 加锁避免多线程并发生成多个对象
            2. 先检测是否有_instance对象，减少加锁操作，提高性能
            3. super().__new__(cls) == super(Single, cls).__new__(cls)
            4. py3 中 __new__ 只接受一个参数，返回实例
            5. 获取到实例后，可以根据*args, **kw 对实例进行修改
        """
        if not cls._instance:
            # 并发可以多个线程达到该位置，获取锁后重新判断实例是否已生成
            with cls._lock:
                if not cls._instance:
                    time.sleep(0.01)
                    cls._instance = super().__new__(cls)
        return cls._instance

def generate(ss, ssn):
    s = Single()
    ss.add(s)

    sn = SingleNoLock()
    ssn.add(sn)

if __name__ == '__main__':
    ths = []
    ss, ssn = set(), set()
    for i in range(1000):
        th = threading.Thread(target=generate, args=(ss, ssn))
        th.setDaemon(True)
        th.start()
        ths.append(th)

    for th in ths:
        th.join()
    print(f'ss len -> {len(ss)}')
    print(f'ssn len -> {len(ssn)}')
