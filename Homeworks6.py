list_ = ['BMW', "MB", "Lada", 'KIA', "Honda"]
string = 'Я езжу на автомабиле марки '
cars_count = 0

for i in range(1):
    print(string, list_[0])
    print(string, list_[1])
    print(string, list_[2])
    print(string, list_[3])
    print(string, list_[4])
    for i in list_:
        cars_count += 10
        print(cars_count)
