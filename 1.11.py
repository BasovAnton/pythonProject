if __name__ == "__main__":
    a = int(input("Введите число a:"))
    b = int(input("Введите число b:"))
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        print("Только одно цисло четное")
    else:
        print("Условие не выполнено")
