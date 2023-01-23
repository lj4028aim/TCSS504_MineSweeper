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

    def test_update_matrix_up_size_3x3(self):
        """Tests update_matrix method at (0,1) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[1, '*', 1], [1, 1, 1], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 0, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_up_right_size_3x3(self):
        """Tests update_matrix method at (0,2) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 1, '*'], [0, 1, 1], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 0, 2)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_right_size_3x3(self):
        """Tests update_matrix method at (1,2) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 1, 1], [0, 1, '*'], [0, 1, 1]]
        mine_sweeper.update_matrix(matrix, 1, 2)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_bottom_size_3x3(self):
        """Tests update_matrix method at (2,1) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 0, 0], [1, 1, 1], [1, '*', 1]]
        mine_sweeper.update_matrix(matrix, 2, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_bottom_left_size_3x3(self):
        """Tests update_matrix method at (2,0) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 0, 0], [1, 1, 0], ['*', 1, 0]]
        mine_sweeper.update_matrix(matrix, 2, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_left_size_3x3(self):
        """Tests update_matrix method at (1,0) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[1, 1, 0], ['*', 1, 0], [1, 1, 0]]
        mine_sweeper.update_matrix(matrix, 1, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_prefilled_neighbors_size_3x3(self):
        """Tests update_matrix method at (1,1) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expect_matrix = [[2, 2, 2], [2, '*', 2], [2, 2, 2]]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_one_updateable_neighbor_size_3x3(self):
        """Tests update_matrix method at (1,1) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[3, '*', '*'], ['*', 0, '*'], ['*', '*', '*']]
        expect_matrix = [[4, '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_sets_mine(self):
        """Tests update_matrix method at (1,1) for a 3x3 matrix, should replace value with '*'  """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertEqual('*', matrix[1][1])

    def test_update_matrix_with_only_mines_size_3x3(self):
        """Tests update_matrix method at (2,2) for a 3x3 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [['*', '*', '*'], ['*', 0, '*'], ['*', '*', '*']]
        expect_matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_only_mines_size_1x100(self):
        """Tests update_matrix method at (0,0) for a 1x100 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [['*'] * 100]
        expect_matrix = [['*'] * 100]
        mine_sweeper.update_matrix(matrix, 0, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_only_mines_size_100x1(self):
        """Tests update_matrix method at (0,0) for a 100x1 matrix filled only mines, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [['*']] * 100
        matrix[0][0] = 0
        expect_matrix = [['*']] * 100
        mine_sweeper.update_matrix(matrix, 0, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_size_1x1(self):
        """Tests update_matrix method at (0,0) for a 1x1, it should not update neighbour
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0]]
        expect_matrix = [['*']]
        mine_sweeper.update_matrix(matrix, 0, 0)
        self.assertListEqual(matrix, expect_matrix)

    # def test_update_matrix_given_invalid_indexes(self):
    #     """Tests update_matrix method at (5,5) for a 2x2 matrix, it should not modify matrix
    #     cells """
    #     mine_sweeper = MineSweeper()
    #     matrix = [[0, 0], [0, 0]]
    #     expect_matrix = [[0, 0], [0, 0]]
    #     mine_sweeper.update_matrix(matrix, 5, 5)
    #     self.assertListEqual(matrix, expect_matrix)

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
