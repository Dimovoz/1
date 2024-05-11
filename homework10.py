def test(*arg):
    print(arg)

test("DD", 23, True)


n = int(input(f'Расчёт факториала: '))
while n < 0:
    print(f'Число должно быть положительным')
    break
else:

    def fact(n):
        a = 1
        for i in range(1, n + 1):
            a *= i
        return a

    print(fact(n))

    def factor(n):
        if n == 0:
            return 1
        else:
            return n * factor(n - 1)

    print(factor(n))
