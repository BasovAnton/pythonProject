def bills(n):

    bills_ = {}
    if n >= 64:
        k = n//64
        bills_["bill_64"] = k
        n = n % 64
    if n >= 32:
        k = n//32
        n = n % 32
        bills_["bill_32"] = k
    if n >= 16:
        k = n//16
        n = n % 16
        bills_["bill_16"] = k
    if n >= 8:
        k = n//8
        n = n % 8
        bills_["bill_8"] = k
    if n >= 4:
        k = n//4
        n = n % 4
        bills_["bill_4"] = k
    if n >= 2:
        k = n//2
        n = n % 2
        bills_["bill_2"] = k
    if n >= 1:
        k = n//1
        bills_["bill_1"] = k

    return bills_


if __name__ == "__main__":
    print(bills(int(input("Введите число: "))))
