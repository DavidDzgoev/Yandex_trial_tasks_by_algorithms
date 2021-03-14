def main():
    number_of_songs = int(input())
    if number_of_songs == 0:
        return

    russian = input()
    foreign = input()

    russian = russian.split()
    foreign = foreign.split()

    russian.reverse()
    foreign.reverse()

    playlist = []

    for i in range(number_of_songs*2):
        if (i+1) % 2 != 0:
            playlist.append(russian.pop())

        if (i+1) % 2 == 0:
            playlist.append(foreign.pop())

    print(' '.join(playlist))


main()
