from math import sqrt

print('Добро пожаловать в самую лучшую программу для '
      'вычисления квадратного корня из заданного числа.')


def calculate_square_root(num):
    """Вычисляет квадратный корень."""
    return sqrt(num)


def calc(your_num):
    """Вычисляет квадратный корень из введенного числа."""
    if your_num <= 0:
        print('Введите другое число')
        return
    csr = calculate_square_root(your_num)
    print(f'Мы вычислили квадратный корень из введённого вами числа.Это будет:'
          f'{csr}')


calc(25.5)
