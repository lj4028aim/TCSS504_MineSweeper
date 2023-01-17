import random

output_file = open("input.txt", "w")


def gen_minefield():
    while True:
        try:
            num_row = int(input("Enter number of rows of the minefield: "))
            num_col = int(input("Enter number of columns of the minefield: "))
            if num_row < 0 or num_col < 0 or num_row > 100 or num_col > 100:
                print("Number of row/column must be between 1 and 100. Or you can enter 0 for both to exit. ")
            elif num_row == 0 and num_col != 0:
                print(f"Number of row/column must be between 1 and 100. Or you can enter 0 for both to exit. ")
            elif num_row != 0 and num_col == 0:
                print(f"Number of row/column must be between 1 and 100. Or you can enter 0 for both to exit. ")
            else:
                if num_row == 0 and num_col == 0:
                    output_file.write(str(0) + " " + str(0))
                    output_file.write("\n")
                    break
                else:
                    mine_percentage = int(input("Enter percentage of mine (1-100): "))
                    minefield_size = str(num_row) + " " + str(num_col)
                    print(minefield_size)
                    output_file.write(minefield_size)
                    output_file.write("\n")
                    for i in range(num_row):
                        for j in range(num_col):
                            num_mines = random.randint(1, 100)
                            if num_mines >= mine_percentage:  # without mines
                                output_file.write(".")
                                print(".", end="")
                            else:  # with mines
                                output_file.write("*")
                                print("*", end="")
                        output_file.write("\n")
                        print()
        except ValueError:
            print("This is not an integer number. ")


gen_minefield()
output_file.close()

