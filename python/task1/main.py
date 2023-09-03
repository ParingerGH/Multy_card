import sys

# Выходим если в $1 не было передано число
if len(sys.argv) < 2:
    print(f"""
    Usage:
    python {__file__} <число>
    """)
    exit(1)

number = int(sys.argv[1])

def is_prime(number:int) -> bool:

    """
    Вычисление "в лоб" через проверку на деление
    """

    # При подсчете простых числе отрицательные и 0 исключены
    # 1-ца по определению не считается простым числом
    if number <= 1:
        return False

    # Если делится хоть на что-то в пределах [2,number-1]
    # то не простое
    for num in range(2, number):
        if number % num == 0:
            return False

    return True

def main():
    print(is_prime(number=number))

if __name__ == "__main__":
    main()
