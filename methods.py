import matplotlib.pyplot as plt
import numpy
def draw_scatter(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
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
    lable_value = combo_value_1 + ' VS ' + combo_value_2
    plt.scatter(values_1, values_2, label=lable_value, marker="*")
    plt.xlabel(combo_value_1)
    plt.ylabel(combo_value_2)
    plt.title(lable_value)
    plt.legend()
    plt.show()


def calculate_cor(combo_1, combo_2, precipitation, water_level, max_temperature, min_temperature, solar_exposure,
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
    values_1 = [float(n) for n in values_1]
    values_2 = [float(n) for n in values_2]
    cor = numpy.corrcoef(values_1, values_2)
    return cor

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