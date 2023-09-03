
if __name__ == "__main__":

    N = 22

    # s: 0   *: 21
    # s: 1   *: 19
    # s: 2   *: 17
    # s: 3   *: 15
    # s: 4   *: 13
    # s: 5   *: 11
    # s: 6   *: 9
    # s: 7   *: 7
    # s: 8   *: 5
    # s: 9   *: 3
    # s: 10  *: 1
    # s: 10  *: 1
    # s: 9   *: 3
    # s: 8   *: 5
    # s: 7   *: 7
    # s: 6   *: 9
    # s: 5   *: 11
    # s: 4   *: 13
    # s: 3   *: 15
    # s: 2   *: 17
    # s: 1   *: 19
    # s: 0   *: 21

    for i in range(N, 0, -1):
        print(f"{N-i} {i-2}")
        #print(" "*(N-i) + "*"*i)


    # with open('chek1.txt') as f:
    #     for lien in f.readlines():

    #         count_star = lien.count("*")
    #         count_space = lien.count(" ")

    #         print(f"s: {count_space}  *: {count_star}")

