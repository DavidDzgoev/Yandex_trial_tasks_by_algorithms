def main():
    r_and_c = int(input())
    if r_and_c < 1 or r_and_c > 1000:
        return

    matrix = []
    for i in range(r_and_c):
        row = input().split(sep=' ')
        for element in row:
            matrix.append(element)

    if r_and_c == 1:
        print(matrix[0])
        return

    def make_spiral_row(mat):
        max_rows = r_and_c
        central_index = int(r_and_c / 2 - 0.5)
        current = [central_index, central_index]

        n_bot_limit = central_index - 1
        n_top_limit = central_index + 1

        m_bot_limit = central_index + 1
        m_top_limit = central_index - 1

        for j in range(int((r_and_c + 1) / 2)):

            for i in range(int(current[1] - m_top_limit)):
                print(mat[int(current[0] + r_and_c * current[1])])
                current[1] -= 1

            m_top_limit -= 1

            if current == [0, -1]:
                break

            for i in range(int(n_top_limit - current[0])):
                print(mat[int(current[0] + r_and_c * current[1])])
                current[0] += 1

            n_top_limit += 1

            for i in range(m_bot_limit - current[1]):
                print(mat[int(current[0] + r_and_c * current[1])])
                current[1] += 1

            m_bot_limit += 1

            for i in range(current[0] - n_bot_limit):
                print(mat[int(current[0] + r_and_c * current[1])])
                current[0] -= 1

            n_bot_limit -= 1

    make_spiral_row(matrix)
    return


main()
