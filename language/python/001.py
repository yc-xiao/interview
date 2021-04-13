"""
    1.单例模式，保证在多线程下只有一个实例
    2.当对象频繁的创建跟销毁时，使用单例可以节约开销
"""

import threading
import random
import time

class Sender(object):
    def __init__(self, receivers=[]):
        self.receivers = receivers

    def add_receivers(self, receiver):
        self.receivers.append(receiver)

    def send(self, msg):
        time.sleep(0.01) # 模拟网络延迟
        count = len(self.receivers) - 1
        assert count >= 0, f'未设置接收方'
        index = random.randint(0, count)
        self.receivers[index].append(msg)

    def show(self):
        for r in self.receivers:
            print(r)
s = Sender()

def test_import():
    from . import s as s1
    from . import s as s2
    assert s1 == s2, f'单例模块导入验证不通过'
    print('单例模块导入验证通过')

def test_decorator():
    # 通过装饰器实现单例，无法避免多线程
    def single(cls):
        _dic = {}
        def handler(*args, **kw):
            if cls not in _dic:
                _dic[cls] = cls(*args, **kw)
            return _dic[cls]
        return handler

    @single
    class Sender2(Sender):
        pass

    s1 = Sender2()
    s2 = Sender2()
    assert s1 == s2, f'单例装饰器验证不通过'
    print('单例装饰器验证通过')

def test_multithreading():
    # 通过装饰器实现单例，无法避免多线程
    class Sender2(object):
        _self = None
        _lock = threading.Lock()
        def __new__(cls, *args, **kw):
            with cls._lock:
                if not cls._self:
                    cls._self = super(Sender2, cls).__new__(cls)
            return cls._self

    s1 = Sender2()
    s2 = Sender2()
    assert s1 == s2, f'单例多线程验证不通过'
    print('单例多线程验证通过')

if __name__ == '__main__':
    test_import()
    test_decorator()
    test_multithreading()
