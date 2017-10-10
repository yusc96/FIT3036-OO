import matplotlib.pyplot as plt
import numpy
from neural import Neural

def get_data(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                 precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key):
    precipitation_list = []
    water_level_list = []
    max_temperature_list = []
    min_temperature_list = []
    solar_exposure_list = []
    for i in precipitation_key:
        precipitation_list.append(precipitation[i].amount)
    for i in water_level_key:
        water_level_list.append(water_level[i].amount)
    for i in max_temperature_key:
        max_temperature_list.append(max_temperature[i].temp)
    for i in min_temperature_key:
        min_temperature_list.append(min_temperature[i].temp)
    for i in solar_exposure_key:
        solar_exposure_list.append(solar_exposure[i].amount)
    combo_value_1 = combo_1.get()
    combo_value_2 = combo_2.get()
    values_1 = None
    values_2 = None
    if combo_value_1 == "Water Level":
        values_1 = water_level_list
    elif combo_value_1 == "Precipitation":
        values_1 = precipitation_list
    elif combo_value_1 == "Max Temperature":
        values_1 = max_temperature_list
    elif combo_value_1 == "Min Temperature":
        values_1 = min_temperature_list
    elif combo_value_1 == "Solar Exposure":
        values_1 = solar_exposure_list
    if combo_value_2 == "Water Level":
        values_2 = water_level_list
    elif combo_value_2 == "Precipitation":
        values_2 = precipitation_list
    elif combo_value_2 == "Max Temperature":
        values_2 = max_temperature_list
    elif combo_value_2 == "Min Temperature":
        values_2 = min_temperature_list
    elif combo_value_2 == "Solar Exposure":
        values_2 = solar_exposure_list
    return [values_1, values_2, combo_value_1, combo_value_2]

def draw_scatter(values_1, values_2, combo_value_1, combo_value_2):
    lable_value = combo_value_1 + ' VS ' + combo_value_2
    plt.scatter(values_1, values_2, label=lable_value, marker="*")
    plt.xlabel(combo_value_1)
    plt.ylabel(combo_value_2)
    plt.title(lable_value)
    plt.legend()
    plt.show()


def draw_scatter_connect(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                 precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key):
    data = get_data(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                 precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key)
    values_1 = data[0]
    values_2 = data[1]
    combo_value_1 = data[2]
    combo_value_2 = data[3]
    draw_scatter(values_1, values_2, combo_value_1, combo_value_2)


def calculate_cor(values_1, values_2):
    values_1 = [float(n) for n in values_1]
    values_2 = [float(n) for n in values_2]
    cor = numpy.corrcoef(values_1, values_2)
    return cor.item(0, 1)


def calculate_cor_connect(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                 precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key):
    data = get_data(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                 precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key)
    values_1 = data[0]
    values_2 = data[1]
    return calculate_cor(values_1, values_2)


def month_con(month):
    if month == "Jan":
        return 1
    elif month == "Feb":
        return 2
    elif month == "Mar":
        return 3
    elif month == "Apr":
        return 4
    elif month == "May":
        return 5
    elif month == "Jun":
        return 6
    elif month == "Jul":
        return 7
    elif month == "Aug":
        return 8
    elif month == "Sep":
        return 9
    elif month == "Oct":
        return 10
    elif month == "Nov":
        return 11
    elif month == "Dec":
        return 12


def making_training_set(precipitation, water_level, max_temperature, min_temperature, solar_exposure,
                      precipitation_key, water_level_key, max_temperature_key, min_temperature_key, solar_exposure_key):
    training_set = []
    for i in range (0, len(precipitation_key)):
        a_record = []
        a_record.append(float(max_temperature[max_temperature_key[i]].temp))
        a_record.append(float(min_temperature[min_temperature_key[i]].temp))
        a_record.append(float(precipitation[precipitation_key[i]].amount))
        a_record.append(float(solar_exposure[solar_exposure_key[i]].amount))
        a_record.append(float(water_level[water_level_key[i]].amount))
        training_set.append(a_record)
    return training_set


def delete_data_rain_0(training_set):
    new_set = training_set
    for i in range(len(new_set)):
        if new_set[i][2] == 0:
            del i
    return new_set


def training_sub(a_train_set, my_neural):
    my_neural.set_i1(a_train_set[0])
    my_neural.set_i2(a_train_set[1])
    my_neural.set_i3(a_train_set[2])
    my_neural.set_i4(a_train_set[3])
    my_neural.set_target((a_train_set[4] + 1) * 1000000)
    my_neural.learn_w1()
    my_neural.learn_w2()
    my_neural.learn_w3()
    my_neural.learn_w4()
    my_neural.learn_b()
    return my_neural


def training(training_set, training_time):
    a_list = []
    neural_1 = Neural()
    for i in range(training_time):
        ri = numpy.random.randint(len(training_set))
        a_train_set = training_set[ri]
        training_sub(a_train_set, neural_1)
        a_list.append(abs((neural_1.output / 1000000) - 1 - a_train_set[4]))
    sum = 0
    for j in a_list:
        sum = sum + j
    avg = sum / len(a_list)
    print('avg_error = ' + str(avg))
    return [neural_1.get_w1(), neural_1.get_w2(), neural_1.get_w3(), neural_1.get_w4(), neural_1.get_b(), a_list]

def draw_scatter_test(y):
    #part_y = []
    #for i in range(0, len(y), 1000):
        #part_y.append(y[i])
    plt.hist(y)
    plt.xlabel("Error")
    plt.ylabel("Frequency")
    plt.title("Prediction Error Histogram")
    plt.show()