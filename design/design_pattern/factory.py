"""
    工厂模式：用户通过选择已有工厂生产(对象)
        1.选择工厂，在选择生产的型号，生成对象
        2.选择型号工厂，直接生成对象
    场景:
        可以通过选择工厂，输入获取对应的类，不需要了解类有什么东东，封装具体类的实现
"""

class AMD(object):
    def show():
        print('AMD YES')

class INTEL(object):
    def show():
        print('INTEL YES')

class CpuFactory(object):
    # 1.通过输入选择型号
    def get(self, cpu):
        if cpu == 'AMD':
            return AMD()
        elif cpu == 'INTEL':
            return INTEL()
        else:
            return None

    # 2.直接选择信号
    def get_amd(self):
        return AMD()

    # 2.直接选择信号
    def get_intel(self):
        return INTEL()

# 3.选择指定工厂生产
class AMDFactory(object):
    def get(self):
        return AMD()

class INTELFactory(object):
    def get(self):
        return INTEL()


if __main__ == '__main__':
    cpu_factory = CpuFactory()
    amd = cpu_factory.get('AMD')
