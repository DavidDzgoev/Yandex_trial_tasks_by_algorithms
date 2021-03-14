def main():
    n = int(input())
    board = [int(i) for i in input().split(sep=' ')]
    k = int(input())

    success = 0

    def unique_pairs(array):
        for i in array:
            for j in array:
                if i != j:
                    yield i, j

    for i, j in unique_pairs(board):
        if i + j == k:
            if i != j:
                success = 1
                print(f'{min([i, j])} {max([i, j])}')
                break

    if success == 0:
        print('None')


main()
