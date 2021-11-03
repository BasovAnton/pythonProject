def deposit(amount):
    if amount <= 5000:
        dep = amount*0.2
        return dep
    elif 5000 < amount <= 10000:
        dep = amount * 0.22
        return dep


if __name__ == "__main__":
    print(deposit(int(input("Введите сумму депозита от 0 до 10000: "))))
