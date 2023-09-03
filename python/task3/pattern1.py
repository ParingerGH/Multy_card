
if __name__ == "__main__":

    N = 21

    stars = N
    for i in range(N, -1, -1):
        print(" "*((N - abs(stars))//2), end="")
        print("*"*abs(stars))
        stars -= 2

