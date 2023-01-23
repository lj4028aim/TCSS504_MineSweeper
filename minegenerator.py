import random


class MinesGenerator:

    def gen_random_minefield(self, array, output_file):
        """
        Method is used to generate desired minefield based on the array passed in and write it into a text file
        as minesweeper_input file against team solution.
        :param array: array is consist of three elements. The first two elements are representing number of rows and
        columns. The third number is representing percentage of mines.
        :param output_file: Output_file is a text file which contains all minefields generated based on the array, and
        it is ended with 0 0.
        :return: None.
        """
        for i in range(len(array)):
            if len(array[i]) == 3:
                num_row, num_col, mine_percentage = map(int, array[i])
                i += 1
                if num_row != 0 and num_col != 0:
                    minefield_size = str(num_row) + " " + str(num_col)
                    output_file.write(minefield_size)
                    output_file.write("\n")
                    for k in range(num_row):
                        for j in range(num_col):
                            num_mines = random.randint(1, 100)
                            if num_mines >= mine_percentage:  # without mines
                                output_file.write(".")
                                # print(".", end="")
                            else:  # with mines
                                output_file.write("*")
                                # print("*", end="")
                        output_file.write("\n")
                        print()
            else:
                output_file.write(str(0) + " " + str(0))
                output_file.write("\n")
                # break
