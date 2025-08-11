###########1. Базовые операции с bool###########

# Создание булевых значений
b1 = True
b2 = False
print(b1)          # True
print(b2)          # False

# Логические операции
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Сравнение значений
print(5 == 5)       # True
print(5 != 3)       # True
print(5 > 3)        # True
print(5 < 3)        # False




###########2. Преобразование других типов в bool###########

# Из чисел
print(bool(1))      # True
print(bool(0))      # False
print(bool(-5))     # True

# Из строк
print(bool("Hello")) # True
print(bool(""))      # False

# Из списков
print(bool([1, 2]))  # True
print(bool([]))      # False

# Из None
print(bool(None))    # False



###########3. Арифметические операции с bool###########

# Bool как подкласс int
print(True + True)   # 2
print(False * 5)     # 0
print(True * 3.14)   # 3.14