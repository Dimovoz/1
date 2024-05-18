x = 38
print('helowa')
if x < 0:
    print('menshe 0')
print('buebue')
# примеры
a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b < 1000):
    print('успех')
if 5 < b and b < 10:
    print('успех')
# Сравнение
if '34' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1,2,4,5,] < [1,3,5,7,]:
    print('успех')
if [1,2,7,34,] > [1,2,9]:
    print('успех')

# Нельзя сравнивать РАЗНЫЕ типы
#if '6' > 6:
    print('успех')
#if [5,6] > 5:
    print('успех')
# НО
if '6' != 5:
    print('успех')
