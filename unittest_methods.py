import unittest
import methods
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

if __name__ == "__main__":
    unittest.main()