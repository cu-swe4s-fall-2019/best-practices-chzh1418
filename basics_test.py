import unittest
import get_column_stats as gcs
import random
import os
import math
import statistics


class TestGetColumnStats(unittest.TestCase):
    def test_mean_cst(self):
        V = list(range(100))
        self.assertEqual(gcs.get_mean(V), statistics.mean(V))

    def test_mean_random(self):
        V = random.sample(range(1, 100), 3)
        self.assertEqual(gcs.get_mean(V), statistics.mean(V))

    def test_mean_Input(self):
        self.assertRaises(TypeError, gcs.get_mean, None)
        self.assertRaises(TypeError, gcs.get_mean, 'Foo')
        self.assertRaises(TypeError, gcs.get_mean, 1)

    def test_stdev_random(self):
        V = random.sample(range(1, 100), 3)
        self.assertAlmostEqual(gcs.get_stdev(V), statistics.stdev(V),
                               places=-2)

    def test_stdev_Input(self):
        self.assertRaises(TypeError, gcs.get_stdev, None)
        self.assertRaises(TypeError, gcs.get_stdev, 'Foo')
        self.assertRaises(TypeError, gcs.get_stdev, 1)


if __name__ == '__main__':
    unittest.main()
