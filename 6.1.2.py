def bills(n):
    bills_ = {}
    list_ = [2**i for i in range(6, -1, -1)]
    for i in list_:
        if n >= i:
            k = int(n//i)
            bills_[f"купюра номиналом {i}"] = k
            n = n % i
    return bills_


if __name__ == "__main__":
    print(bills(int(input("Введите число: "))))
