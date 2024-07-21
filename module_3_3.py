#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

#2
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = ["Mikhail", 15, False]
values_dict = {'a': 937, 'b': False, 'c': "Ура, Ура!"}
print_params(*values_list)
print_params(**values_dict)

#3
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list2 = ["Gevorgyan", 15]
print_params(*values_list2, 99)
