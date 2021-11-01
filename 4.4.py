def uneven_multiple_of_five(n):
    return [i for i in range(10, n+1) if i % 2 != 0 and i % 5 == 0]


if __name__ == "__main__":
    print(uneven_multiple_of_five(int(input("Введите число N: "))))
