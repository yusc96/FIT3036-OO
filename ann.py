from neural import Neural
import numpy
my_trainset = [[24.2, 19.8, 0, 22, 0.095],
               [27.6, 17.1, 0, 25.1, 0.037],
               [27.1, 17.5, 0, 25.7, -0.11],
               [26, 16.3, 0, 15.3, -0.225],
               [25.7, 17.1, 0, 25.8, -0.202],
               [25.7, 17.3, 0, 18.1, -0.09],
               [21.3, 16.3, 0, 30.4, -0.074],
               [20.6, 16.2, 0, 25.4, -0.116],
               [21.4, 16.8, 0, 21.3, -0.131]]


def training_ann(training_set, my_neural):
    my_neural.set_w1(training_set[0])
    my_neural.set_w2(training_set[1])
    my_neural.set_w3(training_set[2])
    my_neural.set_w4(training_set[3])
    my_neural.set_target(training_set[4])
    my_neural.learn_w1()
    my_neural.learn_w2()
    my_neural.learn_w3()
    my_neural.learn_w4()
    my_neural.learn_b()
    return my_neural



neural_1 = Neural(24.2, 19.8, 0, 22, 0.095)
for i in range(50000):
    ri = numpy.random.randint(len(my_trainset))
    train_set = my_trainset[ri]
    training_ann(train_set, neural_1)
    print(neural_1.cal_new_i())

