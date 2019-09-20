import unittest
import get_column_stats
import random
import os
import math


class TestGetColumnStats(unittest.TestCase):
    def setUp(self):
        self.testcase1 = [1, 1, 1]

    def test_testcase1(self):
        self.assertEqual(get_column_stats.get_mean(self.testcase1), 1)

    @classmethod
    def setUpClass(cls):
        cls.class_test_file_name = 'class_setup_test_file.txt'
        f = open(cls.class_test_file_name, 'w')
        cls.vector = []
        for i in range(1, 100):
            rand_int = random.randint(1, 100)
            cls.vector.append(rand_int)
            f.write(str(rand_int) + '\n')
        cls.mean = sum(cls.vector)/100
        cls.sd = math.sqrt(sum([(cls.mean-x)**2 for x in cls.vector]) / 100)
        f.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.class_test_file_name)

    def test_file_mean_class_setup(self):
        file_mean = get_column_stats.get_mean(self.class_test_file_name)
        self.assertEqual(file_mean, self.file_mean)

    def test_file_stdev_class_setup(self):
        file_stdev = get_column_stats.get_stdev(self.class_test_file_name)
        self.assertEqual(file_stdev, self.file_stdev)


if __name__ == '__main__':
    unittest.main()
