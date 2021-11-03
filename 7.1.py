if __name__ == "__main__":
    n = int(input("Введите размер таблицы умножения: "))
    matrix = [
        [i*j for j in range(1, n+1)]
        for i in range(1, n+1)]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ceil = matrix[row][col]
            print(f'{ceil:5}', end=" ")
        print()
