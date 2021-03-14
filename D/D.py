def main():
    row_and_columns = int(input())
    if row_and_columns < 1 or row_and_columns > 1000:
        return

    matrix = []
    for i in range(row_and_columns):
        row = input().split(sep=' ')
        for element in row:
            matrix.append(element)

    if row_and_columns == 1:
        print(matrix[0])
        return

    def make_spiral_row(mat):
        max_rows = row_and_columns
        central_index = int(row_and_columns / 2 - 0.5)
        current = [central_index, central_index]

        column_bot_limit = central_index - 1
        column_top_limit = central_index + 1

        row_bot_limit = central_index + 1
        row_top_limit = central_index - 1

        for circle in range(int((row_and_columns + 1) / 2)):

            for up in range(int(current[1] - row_top_limit)):
                print(mat[int(current[0] + row_and_columns * current[1])])
                current[1] -= 1

            row_top_limit -= 1

            # end check
            if current == [0, -1]:
                break

            for right in range(int(column_top_limit - current[0])):
                print(mat[int(current[0] + row_and_columns * current[1])])
                current[0] += 1

            column_top_limit += 1

            for down in range(row_bot_limit - current[1]):
                print(mat[int(current[0] + row_and_columns * current[1])])
                current[1] += 1

            row_bot_limit += 1

            for left in range(current[0] - column_bot_limit):
                print(mat[int(current[0] + row_and_columns * current[1])])
                current[0] -= 1

            column_bot_limit -= 1

    make_spiral_row(matrix)
    return


main()
