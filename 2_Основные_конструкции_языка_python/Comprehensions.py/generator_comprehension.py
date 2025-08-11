##🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀 Generator Comprehension (генератор выражений) 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
# Синтаксис:
# (выражение for элемент in итерируемый_объект if условие)
#
# Особенности:
#
# Ленивые вычисления (элементы генерируются по одному)
#
# Потребляют меньше памяти, чем списки

# Примеры:

# Генератор квадратов чисел
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# Фильтрация строк
lines = ["  hello  ", "  world  ", "  python  "]
trimmed = (line.strip() for line in lines)
print(" ".join(trimmed))  # "hello world python"