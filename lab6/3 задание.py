import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result


class TestFactorial(unittest.TestCase):

    #1. Проверяем что 0! = 1
    def test_f_of_zero(self):
        self.assertEqual(factorial(0), 1)

    #2. Проверяем что 1! = 1
    def test_f_of_one(self):
        self.assertEqual(factorial(1), 1)

    #3.Тест положительных чисел
    def test_f_of_posit_num(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)

    #4. Тест обработки ошибок
    def test_f_minus(self):
        self.assertRaises(ValueError, factorial, -7)

    #5.Тест
    def test_f(self):
        n = 15
        self.assertTrue(factorial(n) > 0)
    #проверяем конкретный случай с большим числом. использую фиксированое число 15 тк оно достатлчно большое.
    #это нужно чтобы узнать, что функция корректно обрабатывает числа, близкие к предельным для типа int

    #6. Тест проверки корректности обработки переполнения
    def test_f_overflow(self):
        n = 1
        while True:
            try:
                factorial(n)
                n += 1
            except ValueError:
                break

        self.assertTrue(factorial(n - 1) > 0)
        with self.assertRaises(ValueError) as context:
            factorial(n)
        self.assertEqual(str(context.exception), f"Факториал для {n} не поддерживается типом int")
    #Этот тест проверяет, что функция factorial() корректно обрабатывает ситуацию переполнения целочисленного
    # типа (int), когда результат становится слишком большим

    #7.Тест проверки корректности вычислений для максимально возможного числа
    def test_f_num(self):
        n = 1
        while True:
            try:
                factorial(n)
                n += 1
            except ValueError:
                break
        self.assertIsInstance(factorial(n - 1), int)
    #Этот тест проверяет работу функции factorial() с максимально большим числом,
    #которое ещё не вызывает переполнение для типа int

    #8.Тест на проверку на целостность числа
    def test_f_invalid_types(self):
        with self.assertRaises(TypeError):
            factorial(1.9)  # Не целое число

    #9.Тест на проверку строки
    def test_f_str(self):
        self.assertRaises(TypeError, factorial, "7") # Проверка строки


if __name__ == '__main__':
    unittest.main()