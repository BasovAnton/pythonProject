def bills(n):
    bills_ = {}
    for i in [1, 2, 4, 8, 16, 32, 64]:
        print(i)

        if n >= (64/i):
            k = n//(64/i)
            bills_[f"купюра номинал {64/i}"] = k
            n = n % (64/i)
    return bills_


if __name__ == "__main__":
    print(bills(int(input("Введите число: "))))
