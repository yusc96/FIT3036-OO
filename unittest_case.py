import unittest
import methods
from precipitation import Precipitation
from temperature import Temperature
from water_level import Water_level
from solar import Solar
from neural import Neural
from window import MainWindow
class Testmethods(unittest.TestCase):

    def test_month_con(self):
        self.assertEqual(methods.month_con('Jan'), 1)
        self.assertEqual(methods.month_con('Feb'), 2)
        self.assertEqual(methods.month_con('Mar'), 3)
        self.assertEqual(methods.month_con('Apr'), 4)
        self.assertEqual(methods.month_con('May'), 5)
        self.assertEqual(methods.month_con('Jun'), 6)
        self.assertEqual(methods.month_con('Jul'), 7)
        self.assertEqual(methods.month_con('Aug'), 8)
        self.assertEqual(methods.month_con('Sep'), 9)
        self.assertEqual(methods.month_con('Oct'), 10)
        self.assertEqual(methods.month_con('Nov'), 11)
        self.assertEqual(methods.month_con('Dec'), 12)

    def test_calculate_cor(self):
        values_1 = [2, 4, 1, 5, 6]
        values_2 = [2, 4, 3, 5, 7]
        self.assertEqual(round(methods.calculate_cor(values_1, values_2), 3), 0.903)
        values_1 = [0.2, 0.4, 0.1, 0.5, 0.6]
        values_2 = [0.2, 0.4, 0.3, 0.5, 0.7]
        self.assertEqual(round(methods.calculate_cor(values_1, values_2), 3), 0.903)
        values_1 = [0.2, -0.4, 0.1, 0.5, 0.6]
        values_2 = [0.2, 0.4, 0.3, 0.5, -0.7]
        self.assertEqual(round(methods.calculate_cor(values_1, values_2), 3), -0.526)

    def test_making_training_set(self):
        precipitation = {170101:Precipitation(17, 1, 1, 20, 123456), 170102:Precipitation(17, 1, 2, 0.5, 123456)}
        water_level = {170101: Water_level(17, 1, 1, 0.5), 170102:Water_level(17, 1, 2, 0.38)}
        max_temperature = {170101:Temperature(17, 1, 1, 30.5, 123456), 170102:Temperature(17, 1, 2, 25.4, 123456)}
        min_temperature = {170101:Temperature(17, 1, 1, 21.3, 123456), 170102:Temperature(17, 1, 2, 19.8, 123456)}
        solar_exposure = {170101:Solar(17, 1, 1, 30.6, 123456), 170102:Solar(17, 1, 2, 20.1, 123456)}
        precipitation_key = [170101, 170102]
        water_level_key = [170101, 170102]
        max_temperature_key = [170101, 170102]
        min_temperature_key = [170101, 170102]
        solar_exposure_key = [170101, 170102]
        result = [[30.5, 21.3, 20, 30.6, 0.5],
                  [25.4, 19.8, 0.5, 20.1, 0.38]]
        self.assertEqual(methods.making_training_set(precipitation, water_level, max_temperature, min_temperature,
                                                     solar_exposure, precipitation_key, water_level_key,
                                                     max_temperature_key, min_temperature_key,
                                                     solar_exposure_key), result)

    def test_neural_cal_new_i(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        result = 64
        self.assertEqual(test_neural.cal_new_i(), result)

    def test_neural_cal_cost(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 1296
        self.assertEqual(test_neural.cal_cost(), result)

    def test_neural_dcost_dz(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -72
        self.assertEqual(test_neural.dcost_dz(), result)

    def test_neural_dcost_dw1(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -144
        self.assertEqual(test_neural.dcost_dw1(), result)

    def test_neural_dcost_dw2(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -216
        self.assertEqual(test_neural.dcost_dw2(), result)

    def test_neural_dcost_dw3(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -288
        self.assertEqual(test_neural.dcost_dw3(), result)

    def test_neural_dcost_dw4(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -360
        self.assertEqual(test_neural.dcost_dw4(), result)

    def test_neural_dcost_db(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = -72
        self.assertEqual(test_neural.dcost_db(), result)

    def test_neural_learn_w1(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 2.00144
        self.assertEqual(test_neural.learn_w1(), result)

    def test_neural_learn_w2(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 3.00216
        self.assertEqual(test_neural.learn_w2(), result)

    def test_neural_learn_w3(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 4.00288
        self.assertEqual(test_neural.learn_w3(), result)

    def test_neural_learn_w4(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 5.0036
        self.assertEqual(test_neural.learn_w4(), result)

    def test_neural_learn_b(self):
        test_neural = Neural()
        test_neural.set_w1(2)
        test_neural.set_w2(3)
        test_neural.set_w3(4)
        test_neural.set_w4(5)
        test_neural.set_b(10)
        test_neural.set_i1(2)
        test_neural.set_i2(3)
        test_neural.set_i3(4)
        test_neural.set_i4(5)
        test_neural.set_target(100)
        result = 10.00072
        self.assertEqual(test_neural.learn_b(), result)

    def test_predict_1(self):
        test_window = MainWindow()
        test_window.w1 = 2
        test_window.w2 = 2.5
        test_window.w3 = 1.45
        test_window.w4 = 3.62
        test_window.b = 5.6
        max_temp = 30
        min_temp = 25.5
        rainfall = 3.4
        solar = 20
        result = -0.99979332
        self.assertEqual(test_window.predict(max_temp, min_temp, rainfall, solar), result)

    def test_predict_2(self):
        test_window = MainWindow()
        test_window.w1 = 2
        test_window.w2 = -2.5
        test_window.w3 = 1.45
        test_window.w4 = -3.62
        test_window.b = 5.6
        max_temp = 30
        min_temp = 25.5
        rainfall = 3.4
        solar = 20
        result = -1.00006562
        self.assertEqual(test_window.predict(max_temp, min_temp, rainfall, solar), result)

    def test_predict_3(self):
        test_window = MainWindow()
        test_window.w1 = 2
        test_window.w2 = 2.5
        test_window.w3 = 1.45
        test_window.w4 = 3.62
        test_window.b = 5.6
        max_temp = 30
        min_temp = 25.5
        rainfall = -3.4
        solar = 20
        result = ValueError
        self.assertEqual(test_window.predict(max_temp, min_temp, rainfall, solar), result)

    def test_predict_4(self):
        test_window = MainWindow()
        test_window.w1 = 2
        test_window.w2 = 2.5
        test_window.w3 = 1.45
        test_window.w4 = 3.62
        test_window.b = 5.6
        max_temp = 'Thirty'
        min_temp = 'twenty five point five'
        rainfall = 'Three Point four'
        solar = 'twenty'
        result = TypeError
        self.assertEqual(test_window.predict(max_temp, min_temp, rainfall, solar), result)

if __name__ == "__main__":
    unittest.main()