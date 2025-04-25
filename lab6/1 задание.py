def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


# 1. Среднее двух одинаковых целых чисел
assert average_num([1, 1]) == 1

# 2. Среднее трех последовательных целых чисел
assert average_num([1, 2, 3]) == 2.0

# 3. Среднее чисел с плавающей точкой
assert average_num([2.5, 3.5, 4.5]) == 3.5

# 4. Обработка пустого списка
try:
    average_num([])
    assert False, "Ожидалась ZeroDivisionError"
except ZeroDivisionError:
    pass

# 5. Строковые представления чисел
assert average_num(["1", "2", "3"]) == 2.0

# 6. Некорректные строки
assert average_num(["a", "b"]) == "Bad request"

# 7. Смешанный список
assert average_num(['1', 'b', '3']) == "Bad request"

# 8. Смешанные типы данных (int, float, строки)
assert average_num([1, 2.5, "3"]) == 2.17

# 9. Большой список чисел
assert average_num([10, 20, 30, 40, 50, 60, 70]) == 40.0

# 10. Список из одного элемента
assert average_num([1]) == 1.0

# 11.Проверка работы с отрицательными
assert average_num([-1, 0, 1]) == 0.0

# 12. Проверка округления до двух знаков после запятой
assert average_num([1, 2]) == 1.5

print("тесты пройдены!")