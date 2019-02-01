import unittest
from preprocess_NLP_pkg.distance_measures import euclidean_distance


class TestDistanceMeasures(unittest.TestCase):

    def test_euclidean_distance_array_3_0_and_array_0_4_is_5(self):
        self.assertTrue(euclidean_distance([3,0],[0,4])==5)

    def test_euclidean_distance_array_0_0_and_array_0_0_is_0(self):
        self.assertTrue(euclidean_distance([0,0],[0,0])==0)

    def test_euclidean_distance_int_5_and_int_3_is_None(self):
        self.assertTrue(euclidean_distance(5,3) is None)




#if __name__ == '__main__':
#unittest.main()