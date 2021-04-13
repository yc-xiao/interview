"""
    建造者模式（Builder Pattern）将一个复杂对象分解成多个相对简单的部分，然后根据不同需要分别创建它们，最后构建成该复杂对象。
        汽车　= 发动机 + 底盘 + 车身
        产品 = 模块A(模块a1, 模块a2, ...) + 模块B(模块b1, 模块b2, ...) + 模块C(模块c1, 模块c2, ...)
        组合使用，Python Logging
    使用场景:
        Logging　组合选择
"""

class Engine():
    def __str__(self):
        return f'Engine'

class Engine2(Engine):
    def __str__(self):
        return f'Engine2'

class Car():
    def __init__(self, engine, chassis, body):
        self.engine = engine
        self.chassis = chassis
        self.body = body

    def show(self):
        return f'{self.engine}, {self.chassis}, {self.body}'

class CarBuilder(object):
    engine = None
    chassis = None
    body = None

    def addEngine(self, engine):
        self.engine = engine

    def addChassis(self, chassis):
        self.chassis = chassis

    def addBody(self, boy):
        self.body = boy

    def build(self):
        return Car(self.engine, self.chassis, self.body)

if __name__ == '__main__':
    carBuilder = CarBuilder()
    carBuilder.addEngine(Engine())
    carBuilder.addBody('boy1')
    carBuilder.addChassis('chassis1')
    car = carBuilder.build()
    print(car.show())

    carBuilder.addEngine(Engine2())
    car2 = carBuilder.build()
    print(car2.show())
