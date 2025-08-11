class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

class LoginTest(BaseTest):  # Наследуем базовый функционал
    def test_valid_login(self):
        self.setup()
        # Тест логина...
        self.teardown()



###############🚀🚀 3. Множественное наследование Класс может наследоваться от нескольких родителей.🚀🚀###############

class Father:
    def skills(self):
        return "Программирование"

class Mother:
    def skills(self):
        return "Рисование"

class Child(Father, Mother):  # Порядок важен!
    def child_skill(self):
        return "Игра на пианино"

# 1. Основная идея примера
# Класс Child наследует методы от обоих родителей (Father и Mother), но:
# Оба родителя имеют метод с одинаковым именем (skills()).
# Python выбирает одну реализацию по правилу MRO (Method Resolution Order).

# Создаем объект
child = Child()
print(child.skills())  # Программирование (первый родитель)



############################### 🚀🚀5. Расширение методов (super())🚀🚀 ##############################
# Если нужно дополнить метод родителя, а не заменить его:


class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # Вызов родительского __init__
        self.student_id = student_id

# Создаем объект
student = Student("Алиса", "S12345")
print(student.name)        # Алиса (из Person)
print(student.student_id)  # S12345 (из Student)

# Важно:
# super() позволяет избежать дублирования кода.



#
############################### 🚀🚀 1. Полное переопределение конструктора (без super()) 🚀🚀 ###############################
# Используется, когда не нужно сохранять логику родителя.

class Animal:
    def __init__(self, name):
        self.name = name
        print("Инициализация Animal")

class Dog(Animal):
    def __init__(self, breed):  # Полностью новый конструктор
        self.breed = breed      # Игнорируем родительский __init__
        print("Инициализация Dog")
