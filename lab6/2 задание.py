def is_palin(s: str) -> bool:

    if not isinstance(s, str):
        raise ValueError("Входные данные должны быть строкой")

    cleaned = ''.join(filter(str.isalnum, s.lower()))
    return cleaned == cleaned[::-1]

# Тесты
def test_palin():
    #1. Русские палиндромы
    assert is_palin("Лёша на полке клопа нашёл")
    assert is_palin("А роза упала на лапу Азора")
    assert is_palin("А как заказ? Казак: — Заказ, как а?")

    #2. Английские палиндромы
    assert is_palin("A man, a plan, a canal: Panama")
    assert is_palin("No lemon, no melon")
    assert is_palin("Was it a car or a cat I saw?")

    #3. Не палиндромы
    assert not is_palin("Скоро сессия")
    assert not is_palin("lazy lazy")
    assert not is_palin("sadfyguhjkll;kjhgf")
    assert not is_palin("Evil is a live")

    #4. Другие случаи
    assert is_palin("")
    assert is_palin("п")  # Один символ рус
    assert is_palin("a")  # Один символ англ
    assert is_palin("1221")
    assert not is_palin("2345679")

    #5. Проверка нестроковых входных данных
    for invalid in [20.1, True, False, None, 42, ["строка"]]:
        try:
            is_palin(invalid)
            assert False, f"Не вызвано исключение для {invalid}"
        except ValueError:
            pass

    print("тесты пройдены!")

test_palin()