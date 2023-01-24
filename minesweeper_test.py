import unittest
from minesweeper import MineSweeper
from minegenerator import MinesGenerator


class MinesweeperTest(unittest.TestCase):
    """
    This class tests functionality MineSweeper class.
    """

    def test_update_matrix_sets_mine(self):
        """Test that update_matrix method sets '*' at (1,1) for a 3x3 matrix  """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertEqual('*', matrix[1][1])

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
        """Tests update_matrix method at (0,1) for a 3x3 matrix filled only 0, it should update adjacent neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[1, '*', 1], [1, 1, 1], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 0, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_up_right_size_3x3(self):
        """Tests update_matrix method at (0,2) for a 3x3 matrix filled only mines, it should update adjacent neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 1, '*'], [0, 1, 1], [0, 0, 0]]
        mine_sweeper.update_matrix(matrix, 0, 2)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_right_size_3x3(self):
        """Tests update_matrix method at (1,2) for a 3x3 matrix filled only mines, it should update adjacent neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 1, 1], [0, 1, '*'], [0, 1, 1]]
        mine_sweeper.update_matrix(matrix, 1, 2)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_bottom_size_3x3(self):
        """Tests update_matrix method at (2,1) for a 3x3 matrix filled only mines, it should not update neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 0, 0], [1, 1, 1], [1, '*', 1]]
        mine_sweeper.update_matrix(matrix, 2, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_bottom_left_size_3x3(self):
        """Tests update_matrix method at (2,0) for a 3x3 matrix filled only mines, it should update adjacent neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[0, 0, 0], [1, 1, 0], ['*', 1, 0]]
        mine_sweeper.update_matrix(matrix, 2, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_left_size_3x3(self):
        """Tests update_matrix method at (1,0) for a 3x3 matrix filled only mines, it should update adjacent neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expect_matrix = [[1, 1, 0], ['*', 1, 0], [1, 1, 0]]
        mine_sweeper.update_matrix(matrix, 1, 0)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_prefilled_neighbors_size_3x3(self):
        """Tests update_matrix method at (1,1) for a 3x3 matrix filled with only hints, it should update adjacent
        neighbour cells """
        mine_sweeper = MineSweeper()
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expect_matrix = [[2, 2, 2], [2, '*', 2], [2, 2, 2]]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_one_updateable_neighbor_size_3x3(self):
        """Tests update_matrix method at (1,1) for a 3x3 matrix with only one updatable cell, it should update one
        neighbor cell """
        mine_sweeper = MineSweeper()
        matrix = [[3, '*', '*'], ['*', 0, '*'], ['*', '*', '*']]
        expect_matrix = [[4, '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_only_mines_size_3x3(self):
        """Tests update_matrix method at (2,2) for a 3x3 matrix filled with only mines, it should not update neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [['*', '*', '*'], ['*', 0, '*'], ['*', '*', '*']]
        expect_matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        mine_sweeper.update_matrix(matrix, 1, 1)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_only_mines_size_1x100(self):
        """Tests update_matrix method at (0,0) for a 1x100 matrix filled with only mines, it should not update neighbour
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

    def test_update_matrix_with_no_mines_size_1x100(self):
        """Tests update_matrix method at (0,50) for a 1x100 matrix filled with no mines, it should update two neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0] * 100]
        expect_matrix = [[0] * 100]
        expect_matrix[0][50] = '*'
        expect_matrix[0][49] = 1
        expect_matrix[0][51] = 1
        mine_sweeper.update_matrix(matrix, 0, 50)
        self.assertListEqual(matrix, expect_matrix)

    def test_update_matrix_with_no_mines_size_100x1(self):
        """Tests update_matrix method at (5,0) for a 100x1 matrix filled with no mines, it should update 2 neighbor
        cells """
        mine_sweeper = MineSweeper()
        matrix = [[0 for x in range(1)] for y in range(100)]
        expect_matrix = [[0 for x in range(1)] for y in range(100)]
        expect_matrix[5][0] = '*'
        expect_matrix[4][0] = 1
        expect_matrix[6][0] = 1
        mine_sweeper.update_matrix(matrix, 5, 0)
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
    #     """Tests update_matrix method at invalid place (5,5) for a 2x2 matrix, it should not modify matrix
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

    def test_read_min_row_col_data_1x1(self):
        """Ensure minesweeper can properly read in the rows, columns, and data for a single minefield."""
        arr = [[1, 1, 50],
               [0, 0]]
        mine_sweeper = MineSweeper()
        mine_generator = MinesGenerator()
        created_input_file = open("test_read_min_row_col_data_1x1.txt", "w")
        mine_generator.gen_random_minefield(arr, created_input_file)
        created_input_file.close()
        input_file = open("test_read_min_row_col_data_1x1.txt", "r")
        input_matrix_size = f"{arr[0][0]} {arr[0][1]}"
        input_array = []  # create an array to hold all data from input file
        while True:
            input_content = input_file.readline().strip()
            if not input_content[0].isnumeric():  # test content if it is a minefield
                array = list(input_content.strip())
                input_array.append(array)
            if input_content[0].isnumeric() and input_content == "0 0":
                break
        input_file.close()
        #  convert matrix back to raw minefield data without updating adjacent number of mines
        input_file = open("test_read_min_row_col_data_1x1.txt", "r")
        output_matrix = mine_sweeper.process_input(input_file)
        for matrix in output_matrix:
            row = len(matrix)
            width = len(matrix[0])
            output_matrix_size = f"{row} {width}"
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != "*":
                        matrix[i][j] = "."
            self.assertEqual(input_matrix_size, output_matrix_size)
            self.assertEqual(input_array, matrix)
        input_file.close()

    def test_read_min_row_col_data_1x100(self):
        """Ensure minesweeper can properly read in the rows, columns, and data for a single minefield."""
        arr = [[1, 100, 50],
               [0, 0]]
        mine_sweeper = MineSweeper()
        mine_generator = MinesGenerator()
        created_input_file = open("test_read_min_row_col_data_1x100.txt", "w")
        mine_generator.gen_random_minefield(arr, created_input_file)
        created_input_file.close()
        input_file = open("test_read_min_row_col_data_1x100.txt", "r")
        input_matrix_size = f"{arr[0][0]} {arr[0][1]}"
        input_array = []  # create an array to hold all data from input file
        while True:
            input_content = input_file.readline().strip()
            if not input_content[0].isnumeric():  # test content if it is a minefield
                array = list(input_content.strip())
                input_array.append(array)
            if input_content[0].isnumeric() and input_content == "0 0":
                break
        input_file.close()
        #  convert matrix back to raw minefield data without updating adjacent number of mines
        input_file = open("test_read_min_row_col_data_1x100.txt", "r")
        output_matrix = mine_sweeper.process_input(input_file)
        for matrix in output_matrix:
            row = len(matrix)
            width = len(matrix[0])
            output_matrix_size = f"{row} {width}"
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != "*":
                        matrix[i][j] = "."
            self.assertEqual(input_matrix_size, output_matrix_size)
            self.assertEqual(input_array, matrix)
        input_file.close()

    def test_read_min_row_col_data_100x1(self):
        """Ensure minesweeper can properly read in the rows, columns, and data for a single minefield."""
        arr = [[100, 1, 50],
               [0, 0]]
        mine_sweeper = MineSweeper()
        mine_generator = MinesGenerator()
        created_input_file = open("test_read_min_row_col_data_100x1.txt", "w")
        mine_generator.gen_random_minefield(arr, created_input_file)
        created_input_file.close()
        input_file = open("test_read_min_row_col_data_100x1.txt", "r")
        input_matrix_size = f"{arr[0][0]} {arr[0][1]}"
        input_array = []  # create an array to hold all data from input file
        while True:
            input_content = input_file.readline().strip()
            if not input_content[0].isnumeric():  # test content if it is a minefield
                array = list(input_content.strip())
                input_array.append(array)
            if input_content[0].isnumeric() and input_content == "0 0":
                break
        input_file.close()
        #  convert matrix back to raw minefield data without updating adjacent number of mines
        input_file = open("test_read_min_row_col_data_100x1.txt", "r")
        output_matrix = mine_sweeper.process_input(input_file)
        for matrix in output_matrix:
            row = len(matrix)
            width = len(matrix[0])
            output_matrix_size = f"{row} {width}"
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != "*":
                        matrix[i][j] = "."
            self.assertEqual(input_matrix_size, output_matrix_size)
            self.assertEqual(input_array, matrix)
        input_file.close()

    def test_read_min_row_col_data_100x100(self):
        """Ensure minesweeper can properly read in the rows, columns, and data for a single minefield."""
        arr = [[100, 100, 50],
               [0, 0]]
        mine_sweeper = MineSweeper()
        mine_generator = MinesGenerator()
        created_input_file = open("test_read_min_row_col_data_100x100.txt", "w")
        mine_generator.gen_random_minefield(arr, created_input_file)
        created_input_file.close()
        input_file = open("test_read_min_row_col_data_100x100.txt", "r")
        input_matrix_size = f"{arr[0][0]} {arr[0][1]}"
        input_array = []  # create an array to hold all data from input file
        while True:
            input_content = input_file.readline().strip()
            if not input_content[0].isnumeric():  # test content if it is a minefield
                array = list(input_content.strip())
                input_array.append(array)
            if input_content[0].isnumeric() and input_content == "0 0":
                break
        input_file.close()
        #  convert matrix back to raw minefield data without updating adjacent number of mines
        input_file = open("test_read_min_row_col_data_100x100.txt", "r")
        output_matrix = mine_sweeper.process_input(input_file)
        for matrix in output_matrix:
            row = len(matrix)
            width = len(matrix[0])
            output_matrix_size = f"{row} {width}"
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != "*":
                        matrix[i][j] = "."
            self.assertEqual(input_matrix_size, output_matrix_size)
            self.assertEqual(input_array, matrix)
        input_file.close()

    def test_read_min_row_col_data_37x49(self):
        """Ensure minesweeper can properly read in the rows, columns, and data for a single minefield."""
        arr = [[37, 49, 50],
               [0, 0]]
        mine_sweeper = MineSweeper()
        mine_generator = MinesGenerator()
        created_input_file = open("test_read_min_row_col_data_37x49.txt", "w")
        mine_generator.gen_random_minefield(arr, created_input_file)
        created_input_file.close()
        input_file = open("test_read_min_row_col_data_37x49.txt", "r")
        input_matrix_size = f"{arr[0][0]} {arr[0][1]}"
        input_array = []  # create an array to hold all data from input file
        while True:
            input_content = input_file.readline().strip()
            if not input_content[0].isnumeric():  # test content if it is a minefield
                array = list(input_content.strip())
                input_array.append(array)
            if input_content[0].isnumeric() and input_content == "0 0":
                break
        input_file.close()
        #  convert matrix back to raw minefield data without updating adjacent number of mines
        input_file = open("test_read_min_row_col_data_37x49.txt", "r")
        output_matrix = mine_sweeper.process_input(input_file)
        for matrix in output_matrix:
            row = len(matrix)
            width = len(matrix[0])
            output_matrix_size = f"{row} {width}"
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != "*":
                        matrix[i][j] = "."
            self.assertEqual(input_matrix_size, output_matrix_size)
            self.assertEqual(input_array, matrix)
        input_file.close()
