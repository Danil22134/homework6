my_dict = {'Danil': 2000, 'Victor': 1977, 'Kristina': 1998}
print(my_dict)
print(my_dict['Danil'])
my_dict['Petya'] = 2008
print(my_dict)
my_dict.update({'Vasya': 2011,
                'Dima': 1994})
print(my_dict)
del my_dict['Victor']
print(my_dict)
print(my_dict.get('Victor'))

my_set = {1, 2, 3, 4, 5, 6, 7, 4, 5, 6}
print(my_set)
my_set.add(8)
my_set.add(9)
print(my_set)
my_set.discard(2)
print(my_set)