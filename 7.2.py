if __name__ == "__main__":
    N = 64
    rabbit_paws = 4
    goose_paws = 2
    max_rabbit = N//rabbit_paws
    for i in (range(1, max_rabbit)):
        rabbit = i
        goose = int((N - i*rabbit_paws)/goose_paws)
        print(f'{rabbit:^2}, {goose:^2}')
