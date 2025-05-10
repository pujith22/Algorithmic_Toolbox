import unittest
from partition_souvenirs import partition3, partition3_naive


class PartitionSouvenirs(unittest.TestCase):
    def test_small(self):
        for values in (
            (20,),
            (7, 7, 7),
            (3, 3, 3),
            (3, 3, 3, 3),
            (3, 4, 3, 4, 3, 4),
            (2,5,3,6,8),
            [2, 1, 9, 13, 13, 9, 1],
            [2, 4, 10, 15, 9, 13, 3, 2, 7, 1],
            [1, 5, 12, 8, 5, 1, 14, 2],
            [15, 7, 11, 9, 3],
            [12, 16, 15, 14, 4, 9, 17, 6, 12]
        ):
            self.assertEqual(partition3(values), partition3_naive(values))

    def test_medium(self):
        for values, answer in (
            ((3, 4, 5, 3, 4, 5, 3, 4, 5), 1)

        ):
            self.assertEqual(partition3(values), answer)


if __name__ == '__main__':
    unittest.main()
