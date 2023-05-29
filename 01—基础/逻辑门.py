"""
File        : 逻辑门
IDE         ：PyCharm 
Author      ：Ethan
Date        ：6/21/2022 10:53 PM 
Description : Python数据结构与算法分析的代码
"""


class LogicGate:
    """逻辑门的父类方法"""

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    # 具体的逻辑
    def performGateLogic(self):
        pass

    def setNextPin(self, source):
        pass


class BinaryGate(LogicGate):
    """二元门"""

    def __init__(self, n):
        # 用来调用父类的构造方法
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    """一元门"""

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("Error, No Empty Pin!")


class AndGate(BinaryGate):
    """与门"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """或门"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    """非门"""

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class Connector:
    """连接器，每个连接器包含两个逻辑门实例"""

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.setNextPin(self)

    def getFrom(self):
        return self.from_gate

    def getTo(self):
        return self.to_gate
