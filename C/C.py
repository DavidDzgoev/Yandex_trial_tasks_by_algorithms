def main():
    users_number = int(input())
    if users_number < 2 or users_number > 10 ** 6:
        return

    active_users_as_string = input()
    active_users = [int(i) for i in active_users_as_string.split(' ')]

    if len(active_users) != users_number - 2:
        return

    active_users = set(active_users)
    all_ids = set(range(1, users_number + 1))

    sorted_diff = [str(i) for i in sorted(all_ids.difference(active_users))]
    print(' '.join(sorted_diff))


main()
