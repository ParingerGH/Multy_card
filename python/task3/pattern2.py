
if __name__ == "__main__":

    N = 20

    stars = N
    for i in range(N, -N-2, -2):
        start = (N+2 - abs(i)) // 2
        print("*"*start + " "*abs(i) + "*"*start)

