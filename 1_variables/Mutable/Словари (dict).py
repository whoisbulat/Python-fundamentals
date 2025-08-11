########### 🚀1. Создание словарей 🚀###########

# Пустой словарь
d = {}
print(d)  # {}

# Создание с элементами
d = {'name': 'Alice', 'age': 25}
print(d)  # {'name': 'Alice', 'age': 25}

# Создание через dict()
d = dict(name='Bob', age=30)
print(d)  # {'name': 'Bob', 'age': 30}

# Из списка кортежей
d = dict([('a', 1), ('b', 2)])
print(d)  # {'a': 1, 'b': 2}




########### 🚀2 Доступ к элементам 🚀###########

d = {'name': 'Alice', 'age': 25}

# Получение значения по ключу
print(d['name'])  # 'Alice'

# Метод get() (безопасный доступ)
print(d.get('age'))  # 25
print(d.get('address'))  # None (нет ошибки)
print(d.get('address', 'N/A'))  # 'N/A' (значение по умолчанию)

# Проверка наличия ключа
print('name' in d)  # True
print('address' not in d)  # True




###########🚀 3. Изменение словарей 🚀###########

d = {'name': 'Alice', 'age': 25}

# Добавление/изменение элемента
d['age'] = 26
d['address'] = 'New York'
print(d)  # {'name': 'Alice', 'age': 26, 'address': 'New York'}

# Обновление словаря
d.update({'age': 27, 'city': 'Boston'})
print(d)  # {'name': 'Alice', 'age': 27, 'address': 'New York', 'city': 'Boston'}

# Удаление элементов
del d['address']
print(d)  # {'name': 'Alice', 'age': 27, 'city': 'Boston'}

popped = d.pop('city')
print(popped)  # 'Boston'
print(d)  # {'name': 'Alice', 'age': 27}

# Удаление последнего добавленного элемента (Python 3.7+)
last = d.popitem()
print(last)  # ('age', 27)
print(d)  # {'name': 'Alice'}

# Очистка словаря
d.clear()
print(d)  # {}




########### 🚀 4. Итерация по словарю 🚀###########

d = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Ключи
print(d.keys())  # dict_keys(['name', 'age', 'city'])
for key in d:
    print(key)  # name age city

# Значения
print(d.values())  # dict_values(['Alice', 25, 'New York'])
for value in d.values():
    print(value)  # Alice 25 New York

# Пары ключ-значение
print(d.items())  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])
for key, value in d.items():
    print(f"{key}: {value}")




########### 🚀 5. Копирование словарей 🚀###########

d = {'a': 1, 'b': 2}

# Поверхностная копия
d_copy = d.copy()
print(d_copy)  # {'a': 1, 'b': 2}

# Глубокая копия
import copy
d_deep = copy.deepcopy(d)




########### 🚀 6. Генераторы словарей 🚀 ###########

# Создание словаря из списка
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Dictionary comprehension
d = {x: x**2 for x in range(5)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}




###########7. Слияние словарей (Python 3.9+)###########

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# Объединение с сохранением последних значений
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}

# Обновление на месте
d1 |= d2
print(d1)  # {'a': 1, 'b': 3, 'c': 4}