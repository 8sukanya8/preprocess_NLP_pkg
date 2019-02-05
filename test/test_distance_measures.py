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
        self.assertTrue(inverse_euclidean_similarity([1,1],[1,1])==1)


class TestManhattanDistance(unittest.TestCase):

    def test_manhattan_distance_array_1_1_and_array_1_1(self):
        self.assertTrue(manhattan_distance([1,1],[1,1]) == 0)

    def test_manhattan_distance_array_1_1_and_array_1_0(self):
        self.assertTrue(manhattan_distance([1,1],[1,0]) == 1)


class TestInverseManhattanSimilarity(unittest.TestCase):

    def test_inverse_manhattan_similarity_array_1_1_and_array_1_1(self):
        self.assertTrue(inverse_manhattan_similarity([1, 1], [1, 1] == 1))

    def test_inverse_manhattan_similarity_array_1_1_and_array_1_10(self):
        self.assertTrue(inverse_manhattan_similarity([1, 1], [1, 0] == 0.5))


class TestNthRoot(unittest.TestCase):

    def test_8th_root_of_256_is_2(self):
        self.assertTrue(nth_root(256,8) == 2)

    def test_1th_root_of_1_is_1(self):
        self.assertTrue(nth_root(1,1) == 1)


class TestMinkowskiDistance(unittest.TestCase):

    def test_minkowski_distance_array_0_0_and_1_1_with_p_1_by_4_is_16(self):
        self.assertTrue(minkowski_distance([0,0],[1,1],0.25) == 16)


class TestsSquareRootSum(unittest.TestCase):

    def test_square_root_sum(self):
        self.assertTrue(square_root_sum([4,4,4,4]) == 8)


class TestCosineSimilarity(unittest.TestCase):

    def test_cosine_similarity(self):
        self.assertAlmostEqual(cosine_similarity([1,1],[1,1]), 1.0)


class TestJaccardSimilarity(unittest.TestCase):

    def test_jaccard_similarity_array_1_1_and_1_1_is_1(self):
        self.assertTrue(jaccard_similarity([1,1],[1,1]) == 1.0)
