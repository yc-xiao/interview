"""
    观察者模式:
        观察者模式: 观察者订阅Subject，Subject通知观察者(一对一)
"""

import abc

class Observer(metaclass=abc.ABCMeta):
    # 子类必须实现该接口
    @abc.abstractmethod
    def update(self, *args, **kw):
        pass

class PersionObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print(self.name, subject.__dict__)

def notify(func):
    def inner(self, *args, **kw):
        func(self, *args, **kw)
        self.notify()
    return inner

class Subject(object):
    observers = []  #  多线程需要加锁

    def update(self, key, value):
        setattr(self, key, value)
        self.notify()

    @notify
    def update2(self, key, value):
        setattr(self, key, value)

    def add_observer(self, observer):
        assert isinstance(observer, Observer), f'观察者错误'
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for o in self.observers:
            o.update(self)



if __name__ == '__main__':
    s = Subject()
    xm = PersionObserver('xm')
    xh = PersionObserver('xh')
    s.add_observer(xm)
    s.add_observer(xh)
    s.update('a', 'a')
    print()
    s.remove_observer(xh)
    s.update('a', 'b')
    print()
    s.add_observer(PersionObserver('xq'))
    s.update2('b', 'b2')
