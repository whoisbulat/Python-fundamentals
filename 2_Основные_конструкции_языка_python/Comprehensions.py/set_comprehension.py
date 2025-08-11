#🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀Set Comprehension (генератор множеств) 🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

# Синтаксис:
# {выражение for элемент in итерируемый_объект if условие}
#
# Примеры:

# Уникальные квадраты чисел
unique_squares = {x**2 for x in [1, 2, 2, 3, 3]}
# {1, 4, 9}

# Буквы в строке без повторений
letters = {char for char in "abracadabra"}
# {'a', 'b', 'c', 'd', 'r'}

# Фильтрация длин слов
words = ["apple", "banana", "cherry"]
long_words = {word for word in words if len(word) > 5}
# {'banana', 'cherry'}




