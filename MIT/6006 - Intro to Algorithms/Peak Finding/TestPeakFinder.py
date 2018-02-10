import unittest

from PeakFinder import PeakFinder


class TestPeakFinder(unittest.TestCase):

    def test_one_dimension_a(self):
        self.assertEqual(
                PeakFinder.one_dimension(
                        [6, 7, 4, 3, 2, 1, 4, 5]
                    ), 
                [7, 5])
        self.assertEqual(
                PeakFinder.one_dimension(
                        [8, 1, 9, 2, 3, 10]
                    ), 
                [8, 9, 10])      
        self.assertEqual(
                PeakFinder.one_dimension(
                        [14, 2, 20]
                    ), 
                [14, 20])


if __name__ == '__main__':
    suite = unittest.main()

