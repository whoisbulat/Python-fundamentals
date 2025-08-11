#🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 Dict Comprehension (генератор словарей) 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

# Синтаксис:
# {ключ: значение for элемент in итерируемый_объект if условие}
#
# Примеры:

# Создание словаря с квадратами чисел
square_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Инверсия ключей и значений
original = {"a": 1, "b": 2}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}

# Фильтрация элементов
grades = {"Alice": 90, "Bob": 45, "Charlie": 85}
passed = {k: v for k, v in grades.items() if v >= 60}
# {'Alice': 90, 'Charlie': 85}