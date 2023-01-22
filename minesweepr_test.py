import unittest
from minesweeper import MineSweeper


class MinesweeperTest(unittest.TestCase):
    """
    This class tests functionality MineSweeper class.
    """
    def test_update_matrix_center_case(self):
        """Tests update_matrix method for center case, it should update all the neighbour cell"""
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[1, 1, 1], [1, '*', 1], [1, 1, 1]]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertEqual(matrix, expect_matrix)

    def test_update_matrix_up_left_corner_case(self):
        """Tests update_matrix method for up_left corner case, it should update all the neighbour cell around the
         up_left corner """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [['*', 1, 0], [1, 1, 0], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 0, 0)
        self.assertEqual(matrix, expect_matrix)

    def test_update_matrix_bottom_right_corner_case(self):
        """Tests update_matrix method for bottom_right corner case, it should update all the neighbour cell around the
        bottom_right corner """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 0, 0], [0, 1, 1], [0, 1, '*']]
        mine_sweeper.update_matrix(matrix, 2, 2)
        self.assertEqual(matrix, expect_matrix)

    def test_matrix_to_string(self):
        """Tests matrix_to_string method, it should convert the matrix to expected string"""
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        convert_string = mine_sweeper.matrix_to_string(matrix)
        expect_string = "000\n000\n000\n"
        self.assertEqual(convert_string, expect_string)

    def test_process_input(self):
        """Tests process_input method, it should process all the matrix to expected matrix"""
        mine_sweeper = MineSweeper()
        input_file = open('test.txt', 'r')
        res = mine_sweeper.process_input(input_file)
        expect_first_matrix = [[1, 1, 1], [1, '*', 1], [1, 1, 1]]
        expect_second_matrix = [[0, 0, 0], [0, 1, 1], [0, 1, '*']]
        for i, matrix in enumerate(res):
            if i == 0:
                self.assertEqual(matrix, expect_first_matrix)
            if i == 1:
                self.assertEqual(matrix, expect_second_matrix)
        input_file.close()
