import unittest
from io import StringIO

from minegenerator import MinesGenerator


class MinegeneratorTest(unittest.TestCase):
    """
    This class tests functionality MineGenerator class.
    """
    def test_gen_random_minefield(self):
        """Tests gen_random_minefield method, the generated input file should contain expected input matrix size."""
        outfile = StringIO()
        mine_generator = MinesGenerator()
        array = [[1, 1, 50],
                 [1, 100, 50],
                 [100, 1, 50],
                 [0, 0]]
        mine_generator.gen_random_minefield(array, outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertIn("1 1\n", content)
        self.assertIn("1 100\n", content)
        self.assertIn("100 1\n", content)
        self.assertIn("0 0\n", content)




