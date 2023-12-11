def print_table(table, start_i, end_i, start_j, end_j, conversion_func=None, whole_table=False):
    """Print formatted values that are used in a table.

    Arguments:
    table -- matrix/table
    start_i -- index of the first row to print
    end_i -- index of the last row to print
    start_j -- index of the first column to print, relative to the row
    end_j -- index of the last column to print
    conversion_func -- conversion function for table entries, None if no conversion needed
    whole_table -- True if printing entire table, False if only upper triangle
    """

    if conversion_func is None:
        conversion_func = lambda x: x

    # Find number of digits of longest number
    max_num_digit = float('-inf')
    for i in range(start_i, end_i + 1):
        for j in range(start_j if whole_table else start_j + i - start_i, end_j + 1):
            string = str(conversion_func(table[i, j]))
            if len(string) > max_num_digit:
                max_num_digit = len(string)
    # Print out relevant elements of table.
    for i in range(start_i, end_i + 1):
        if not whole_table:
            for j in range(start_j, start_j + i - start_i):
                print(' ' * max_num_digit, end=" ")
        for j in range(start_j if whole_table else start_j + i - start_i, end_j + 1):
            string = str(conversion_func(table[i, j]))
            print(string.rjust(max_num_digit), end=" ")
        print()
