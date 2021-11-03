def entry(two_digit_nm, number):
    list_ = [int(i) for i in str(two_digit_nm)]
    if number in list_:
        return f"Цифра {number} входит в двухзначное число."
    else:
        return "Не входит."


if __name__ == "__main__":
    print(entry(int(input("Введите двухзначное число: ")),
                int(input("Введите цифру, входимость которой нужно проверить: "))))
