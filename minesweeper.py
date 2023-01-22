from minegenerator import MinesGenerator


class MineSweeper:
    """
    This the solution class
    """

    def update_matrix(self, matrix, i, j):
        """
        update a value inside two-dimensional array .
        :param matrix: two-dimensional array
        :param i: int
        :param j: int
        :return: none
        """
        matrix[i][j] = "*"
        for k in range(-1, 2):
            for l in range(-1, 2):
                if 0 <= i + k < len(matrix) and 0 <= j + l < len(matrix[0]) and matrix[i + k][j + l] != "*":
                    matrix[i + k][j + l] += 1

    def matrix_to_string(self, matrix):
        """
        converted a two-dimensional array to a string.
        :param matrix: two-dimensional array
        :return: string
        """
        res = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += str(matrix[i][j])
            res += "\n"
        return res

    def process_input(self, input_data):
        """
        method to process input data, create matrix by the matrix size. According to each cell value calling
        update_matrix method to update value inside matrix.
        :param input_date: input_file
        :return: yield to all matrix
        """
        while True:
            matrix_size = input_data.readline().strip()
            if matrix_size == "0 0":
                return
            row, width = map(int, matrix_size.split())
            matrix = [[0 for x in range(width)] for y in range(row)]
            for i in range(row):
                line = input_data.readline()
                for j, cha in enumerate(line):
                    if cha == "*":
                        self.update_matrix(matrix, i, j)
            yield matrix

    def main(self, input_data, output):
        """The main method to start process input file and write to the output file"""
        for i, matrix in enumerate(self.process_input(input_data)):
            output.write("Field #%s:\n" % (i + 1))
            output.write(self.matrix_to_string(matrix))
            output.write("\n")


if __name__ == '__main__':
    a = [[1, 1, 50],
         [1, 100, 50],
         [100, 1, 50],
         [0, 0]]

    mine_generator = MinesGenerator()
    mines_sweeper = MineSweeper()

    created_input = open("input.txt", "w")
    mine_generator.gen_random_minefield(a, created_input)
    created_input.close()

    input_file = open('mines.txt', 'r')
    output_file = open('minesweeper_output.txt', 'w')
    mines_sweeper.main(input_file, output_file)
