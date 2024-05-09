def print_param(a=35, b='height', c=True):
    print(a, b, c)


print_param()
print_param(b=25)
print_param(c=[1, 3, 5])

value_list = [23, 'name', False]
value_dict = {'a': 13, 'b': 'weight', 'c': True}

print_param(*value_list)
print_param(**value_dict)

value_list_2 = [4 ,'string']

print_param(*value_list_2, 55)