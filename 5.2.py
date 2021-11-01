def training(n_km, y, x):
    sum_way = 0
    for i in range(x):
        sum_way += n_km
        n_km += n_km*y/100
    return sum_way


if __name__ == "__main__":
    print(f'Суммарный путь: {training(10, 3, 3):.2f}')
