import unittest


from api import get_max_apples

class TestMaxApples(unittest.TestCase):

	def test_max_apples(self):
		A = [3, 4, 1, 7, 8, 5]
		K = 2
		L = 3
		result = get_max_apples(A, K, L)
		self.assertEqual(result, 27)
	
	def test_max_apples(self):
		A = [4, 8, 7, 10, 11]
		K = 2
		L = 2
		result = get_max_apples(A, K, L)
		self.assertEqual(result, 36)


if __name__ == '__main__':
    unittest.main(verbosity=3)
