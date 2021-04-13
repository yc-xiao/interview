"""
    观察者模式-发布订阅模式: 观察者订阅多个Subject，发布者将信息发布到对应的Subject通道，
        观察者从对应Subject通道取出信息(多个频道+多个消息队列+多个观察者)
"""
from uuid import uuid4

class Subject:

    def __new__(cls, *args, **kw):
        """ 给每个subject分配唯一的id """
        obj = super().__new__(cls)
        obj.id = uuid4().hex
        return obj

    def __init__(self):
        self._channel_map = {}

    def push(self, channel_name, msg):
        info = (self.id, f'热点{channel_name}发布信息->{msg}')
        self._channel_map[channel_name].receive(info)

    def set_channel(self, channel):
        self._channel_map[channel.name] = channel

    def remove_channel(self, channel_name):
        self._channel_map.pop(channel_name, None)

    def show_channel(self):
        print(' '.join(self._channel_map.keys()))

class Channel:

    def __init__(self, name):
        self.name = name
        self._observers = []

    def receive(self, info):
        subject_id, msg = info
        for o in self._observers:
            o.receive(msg)

class Observer:
    def __init__(self, name):
        self.name = name

    def add_channel(self, c):
        c._observers.append(self)

    def remove_channel(self, c):
        c._observers.remove(self)

    def receive(self, msg):
        print(f'{self.name}　接受信息: {msg}')

def test():
    s1 = Subject()
    s2 = Subject()

    o1 = Observer('o1')
    o2 = Observer('o2')
    o3 = Observer('o3')

    s1c1 = Channel('s1 top1')
    s1c2 = Channel('s1 top2')
    s2c1 = Channel('s2 top1')
    s2c2 = Channel('s2 top2')


    s1.set_channel(s1c1)
    s1.set_channel(s1c2)
    s2.set_channel(s2c1)
    s2.set_channel(s2c2)

    o1.add_channel(s1c1)
    o2.add_channel(s1c2)
    o3.add_channel(s1c1)
    o3.add_channel(s1c2)
    s1.push('s1 top1', 'hello top1')
    s1.push('s1 top2', 'hello top2')
    s2.push('s2 top1', 'hello top3')


if __name__ == '__main__':
    test()
