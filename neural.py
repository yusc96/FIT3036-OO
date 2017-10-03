import numpy
class Neural:
    def __init__(self):
        self.w1 = numpy.random.randn()
        self.w2 = numpy.random.randn()
        self.w3 = numpy.random.randn()
        self.w4 = numpy.random.randn()
        self.b = numpy.random.randn()
        self.i1 = None
        self.i2 = None
        self.i3 = None
        self.i4 = None
        self.i5 = None
        self.output = None
        self.learning_rate = 0.00001

    def get_w1(self):
        return self.w1

    def get_w2(self):
        return self.w2

    def get_w3(self):
        return self.w3

    def get_w4(self):
        return self.w4

    def set_w1(self, new_w1):
        self.w1 = new_w1

    def set_w2(self, new_w2):
        self.w2 = new_w2

    def set_w3(self, new_w3):
        self.w3 = new_w3

    def set_w4(self, new_w4):
        self.w4 = new_w4

    def get_target(self):
        return self.i5

    def get_b(self):
        return self.b

    def set_target(self, new_target):
        self.i5 = new_target

    def set_i1(self, i1):
        self.i1 = i1

    def set_i2(self, i2):
        self.i2 = i2

    def set_i3(self, i3):
        self.i3 = i3

    def set_i4(self, i4):
        self.i4 = i4

    def cal_new_i(self):
        new_i = self.w1 * self.i1 + self.w2 * self.i2 +\
                self.w3 * self.i3 + self.w4 * self.i4 +\
                self.b
        self.output = new_i
        return new_i

    def cal_cost(self):
        cost = numpy.square(self.cal_new_i()- self.get_target())
        return cost

    def dcost_dz(self):
        answer = 2 * (self.cal_new_i() - self.get_target())
        return answer

    def dz_dw1(self):
        answer = self.i1
        return answer

    def dz_dw2(self):
        answer = self.i2
        return answer

    def dz_dw3(self):
        answer = self.i3
        return answer

    def dz_dw4(self):
        answer = self.i4
        return answer

    def dz_db(self):
        return 1

    def dcost_dw1(self):
        answer = self.dcost_dz() * self.dz_dw1()
        return answer

    def dcost_dw2(self):
        answer = self.dcost_dz() * self.dz_dw2()
        return answer

    def dcost_dw3(self):
        answer = self.dcost_dz() * self.dz_dw3()
        return answer

    def dcost_dw4(self):
        answer = self.dcost_dz() * self.dz_dw4()
        return answer

    def dcost_db(self):
        answer = self.dcost_dz() * self.dz_db()
        return answer

    def learn_w1(self):
        self.w1 = self.w1 - self.learning_rate * self.dcost_dw1()
        return self.w1

    def learn_w2(self):
        self.w2 = self.w2 - self.learning_rate * self.dcost_dw2()
        return self.w2

    def learn_w3(self):
        self.w3 = self.w3 - self.learning_rate * self.dcost_dw3()
        return self.w3

    def learn_w4(self):
        self.w4 = self.w4 - self.learning_rate * self.dcost_dw4()
        return self.w4

    def learn_b(self):
        self.b = self.b - self.learning_rate * self.dcost_db()
        return self.b
