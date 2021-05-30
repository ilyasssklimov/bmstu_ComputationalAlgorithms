from newton import get_xi, get_polynomial, interpolation_newton
from spline import create_spline, interpolation_spline


def f(x):
    return x ** 2


def get_table(n):
    x, y = [], []
    for x_cur in range(n):
        x.append(x_cur)
        y.append(f(x_cur))
    return x, y


def print_result(y_real, y_spline, y_newton, diff_spline, diff_newton):
    print('-' * 65)
    print(f'Значение y(x) = {y_real:.6f}')
    print(f'Результат интерполяции сплайном = {y_spline:.6f}')
    print(f'Относительная погрешность = {diff_spline * 100:.6f}%')
    print(f'Результат интерполяции полиномом Ньютона 3й степени = {y_newton:.6f}')
    print(f'Относительная погрешность = {diff_newton * 100:.6f}%')
    print('-' * 65)


def main():
    try:
        x = float(input('Введите x: '))
    except ValueError:
        return print('Вы должны ввести число')

    x_table, y_table = get_table(11)
    y_real = f(x)
    y_spline = interpolation_spline(create_spline(x_table, y_table), x)
    y_newton = interpolation_newton(get_polynomial(get_xi(3, x), y_table), x)
    diff_spline = abs(y_real - y_spline) / abs(y_real)
    diff_newton = abs(y_real - y_newton) / abs(y_real)
    print_result(y_real, y_spline, y_newton, diff_spline, diff_newton)


if __name__ == '__main__':
    main()
