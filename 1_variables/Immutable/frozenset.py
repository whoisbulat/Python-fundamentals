###########Создание frozenset###########

# Из списка (дубли удаляются)
fs = frozenset([1, 2, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# Из строки (уникальные символы)
fs_str = frozenset("hello")
print(fs_str)  # frozenset({'h', 'e', 'l', 'o'})

# Пустой frozenset
empty_fs = frozenset()
print(empty_fs)  # frozenset()



###########Базовые операции###########

fs = frozenset([1, 2, 3])

# Проверка вхождения
print(2 in fs)  # True

# Размер
print(len(fs))  # 3

# Итерация
for num in fs:
    print(num)  # 1, 2, 3 (порядок не гарантирован)

