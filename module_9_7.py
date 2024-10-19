from math import sqrt

Number = int | float


def prime_check(x: int) -> bool:
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def is_prime(func):
    """
    Функция декоратор, которая распечатывает
    "Простое", если результат 1ой функции будет простым числом
    и "Составное" в противном случае.
    :param func: функция
    :return:
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Простое" if prime_check(result) else "Составное")
        return result
    """
    @is_prime - декоратор для функции sum_three
    """
    return wrapper


@is_prime
def sum_three(a: Number, b: Number, c: Number) -> Number:
    """
    Складывает 3 числа
    :param b: число
    :param a: число
    :param c: число
    :return: сумма a+b+c
    """
    return a + b + c


def test1():
    for i in range(20):
        print(is_prime(lambda x: x)(i))

    result = sum_three(12, 0, 0)
    print(result)


def test():
    result = sum_three(2, 3, 6)
    print(result)
    """
    Результат консоли:
    Простое
    11
    """


if __name__ == '__main__':
    test1()
    test()


"""
2023/12/05 00:00|Домашнее задание по теме "Декораторы"
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

Файл module_9_7.py и загрузите его на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""