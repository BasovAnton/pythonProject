def pre_condition():
    i = 10
    while i <= 30:
        print(i)
        i += 1


def post_condition():
    i = 10
    while True:
        print(i)
        i += 1
        if i > 30:
            break


if __name__ == "__main__":
    pre_condition()
    print('-----')
    post_condition()
