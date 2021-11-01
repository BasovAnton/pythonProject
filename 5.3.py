def number(n):
    n = [int(i) for i in str(n)]
    even = 0
    uneven = 0
    for i in n:
        if i % 2 == 0:
            even += 1
        else:
            uneven += 1
    return f"Количество четных чисел: {even}, количество нечетных чисел: {uneven}."


if __name__ == "__main__":
    print(number(int(input("Введите число: "))))
