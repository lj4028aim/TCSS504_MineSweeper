input_file = open("input.txt", "r")
output_file = open("minesweeper_output.txt", "w")


def gen_new_array():
    """
    Function is used to input each line's content and transfer it into an array for processing
    :return: array transferred from each line's content
    """
    new_array = []
    count = 0
    while True:
        line = input_file.readline()
        if not line[0].isnumeric():  # test content if it is a minefield
            array = list(line.strip())
            new_array.append(array)
        if line[0].isnumeric():  # test content if it is a numeric value
            size = str(line.strip())  # get the size of each minefield
            row = int(size.split(" ")[0])
            col = int(size.split(" ")[1])
            if row != 0 and col != 0:  # start counting field number
                if count != 0:
                    text = "Field #" + str(count) + ":"
                    output_file.write(text)
                    output_file.write("\n")
                    update_array(new_array)
                    write_output(new_array)
                    new_array = []
                    output_file.write("\n")
            else:  # break while loop when hit 0 0
                break
            count += 1
    text = "Field #" + str(count) + ":"
    output_file.write(text)
    output_file.write("\n")
    update_array(new_array)
    write_output(new_array)


def count_adjacent_mines(new_array, row, col):
    """  Function is used to return number of mines at each square of its 8 adjacent squares

    :param new_array: array transferred from input file
    :param row: row number
    :param col: column number
    :return: number of mines of 8 adjacent squares
    """
    num_of_mines = 0
    dirs = [[-1, 0],
            [-1, 1],
            [-1, -1],
            [0, 1],
            [0, -1],
            [1, 1],
            [1, 0],
            [1, -1]]
    for dir in dirs:  # loop through each one of 8 adjacent elements
        nextrow = dir[0] + row
        nextcol = dir[1] + col
        if 0 <= nextrow < len(new_array) and 0 <= nextcol < len(new_array[nextrow]) and new_array[nextrow][nextcol] == "*":
            num_of_mines += 1
    return num_of_mines


def update_array(new_array):
    """  Function is used to return an updated array where '*' is used to depict mine and a specific numeric number
    is used to represent number of mine of its 8 adjacent squares.

    :param new_array: array transferred from input file
    :return: updated array to mimic minefield where '*' stands for mine and number stands for adjacent mines
    """
    updated_array = new_array
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            if new_array[i][j] != "*":  # only replace element which is not equal to '*'
                updated_array[i][j] = count_adjacent_mines(new_array, i, j)
    return updated_array


def write_output(updated_array):
    """
    Function is used to capture output and write it into text file
    :param updated_array:
    :return: updated array to mimic minefield where '*' stands for mine and number stands for adjacent mines
    """
    for i in range(len(updated_array)):
        for j in range(len(updated_array[i])):
            output_file.write(str(updated_array[i][j]))
        output_file.write("\n")

gen_new_array()
# close out input and output files
input_file.close()
output_file.close()
