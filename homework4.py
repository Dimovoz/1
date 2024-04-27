mutable_list = [45,46]
print(mutable_list)
immutable_var = 1,4,'wally',mutable_list
print(immutable_var)
#immutable_var[1] = 6 #меняем значение 4 на 6
print(immutable_var)# TypeError: 'tuple' object does not support item assignment
mutable_list[0] = 95
print(mutable_list)
print(immutable_var) # поменял элемент кортежа