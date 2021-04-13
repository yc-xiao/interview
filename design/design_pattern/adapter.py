"""
    适配器模式: 中间模块，解决两个接口不兼容问题
    使用场景:
        1.旧代码不兼容新版本，可以加适配器处理
"""

class Persion(object):
    def show(self):
        print('this is a persion')

class Student(Persion):
    def show(self):
        print('this is a student')

class Student2(object):
    def __init__(self, msg=None):
        self.msg = msg

    def show(self, msg):
        print(msg)

def adapter(obj):
    if isinstance(obj, Persion):
        obj.show()
    else:
        obj.show(obj.msg)

def run(s):
    # s.show() # 无法直接调用show()，通过adapter适配器处理
    adapter(s)

if __name__ == '__main__':
    s = Student()
    s2 = Student2('this is a student2')
    run(s)
    run(s2)
