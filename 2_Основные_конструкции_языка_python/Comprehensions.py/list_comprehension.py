#🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 1. List Comprehension (генератор списков) 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
#
# Синтаксис:
# [выражение for элемент in итерируемый_объект if условие]

# Примеры:

# 🔹🔹🔹Создание списка квадратов чисел🔹🔹🔹
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# 🔹🔹🔹Фильтрация чётных чисел🔹🔹🔹
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# 🔹🔹🔹Обработка строк🔹🔹🔹
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
# ['HELLO', 'WORLD', 'PYTHON']


# 🔹🔹🔹 С условием if 🔹🔹🔹
# Только чётные квадраты
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Результат: [0, 4, 16, 36, 64]

