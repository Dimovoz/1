print('ENTER NUMBER: ')


def passkey(num_):
    pass_ = ""
    for i in range(1, num_):
        for j in range(i + 1, num_):
            if num_ % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_


print(passkey(int(input())))
