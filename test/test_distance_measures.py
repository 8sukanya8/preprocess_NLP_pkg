import unittest
from preprocess_NLP_pkg.distance_measures import *


class TestEuclideanDistanceMeasures(unittest.TestCase):

    def test_euclidean_distance_array_3_0_and_array_0_4_is_5(self):
        self.assertTrue(euclidean_distance([3,0],[0,4])==5)

    def test_euclidean_distance_array_0_0_and_array_0_0_is_0(self):
        self.assertTrue(euclidean_distance([0,0],[0,0])==0)

    def test_euclidean_distance_int_5_and_int_3_is_None(self):
        self.assertTrue(euclidean_distance(5,3) is None)


class TestInverseEuclideanSimilarity(unittest.TestCase):

    def test_inverse_euclidean_similarity(self):
        pass


class TestManhattanDistance(unittest.TestCase):

    def test_manhattan_distance(self):
        pass


class TestInverseManhattanSimilarity(unittest.TestCase):

    def test_inverse_manhattan_similarity(self):
        pass


class TestNthRoot(unittest.TestCase):

    def test_nth_root(self):
        pass


class TestMinkowskiDistance(unittest.TestCase):

    def test_minkowski_distance(self):
        pass


class TestsSquareRootSum(unittest.TestCase):

    def test_square_root_sum(self):
        pass


class TestCosineSimilarity(unittest.TestCase):

    def test_cosine_similarity(self):
        pass


class TestJaccardSimilarity(unittest.TestCase):

    def test_jaccard_similarity(self):
        pass
