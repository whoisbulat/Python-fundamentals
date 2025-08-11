# 1. f-строки (форматированные строки)
name = "Булат"
# Простая f-строка
message = f"Меня зовут {name}."


# Конкатенация (сложение строк)
greet = "Hello" + " " + "World"  # "Hello World"


# Повторение строки
stars = "*" * 5  # "*****"


# Длина строки
length = len("Python")  # 6


# Доступ к символам по индексу
s = "Python"
first_char = s[0]   # 'P' (первый символ)
last_char = s[-1]    # 'n' (последний символ)


# 2. replace() — замена подстроки
text = "Я люблю Яблоки"
new_text = text.replace("яблоки", "бананы")
print(new_text)  # "Я люблю бананы"


# Замена с ограничением количества замен
limited = text.replace("Я", "я",2)
print(limited)  # "я люблю яблоки" (заменил только 2 первых "я")


# Удаление символов (замена на пустую строку)
no_spaces = text.replace(" ", "")
print(no_spaces)  # "Ялюблюяблоки"


# Регистр символов
s = "Hello, World!"
print(s.upper())      # "HELLO, WORLD!"
print(s.lower())      # "hello, world!"
print(s.title())      # "Hello, World!"
print(s.swapcase())   # "hELLO, wORLD!"


# Удаление пробелов
s = "  hello  "
print(s.strip())   # "hello" (обрезает пробелы с двух сторон)
print(s.lstrip())  # "hello  " (обрезает слева)
print(s.rstrip())  # "  hello" (обрезает справа)


# Разделение и соединение строк split
csv = "apple,banana,orange"
fruits = csv.split(",")  # ['apple', 'banana', 'orange']

text = "Line1\nLine2\nLine3"
lines = text.splitlines()  # ['Line1', 'Line2', 'Line3']


# Соединение (join)
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"



# В Python срезы (slicing) позволяют извлекать части строк или списков. Вот несколько наглядных примеров срезов со строками:
#
# Основной синтаксис:
# python
# s[start:stop:step]
# start - индекс начала (включительно)
#
# stop - индекс конца (не включается)
#
# step - шаг (по умолчанию 1)

# Примеры срезов:
# Удаление первого и последнего символа (ваша задача):


s = "пример"
print(s[1:-1])  # "риме"
# s[1] -> 'р' (второй символ)
# s[-1] -> 'р' (последний символ)
# s[1:-1] -> от второго до предпоследнего

#Разворот строки:

s = "привет"
print(s[::-1])