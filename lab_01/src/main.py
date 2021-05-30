from func import get_diff, get_xi_newton, get_xi_hermit, get_xi_reverse
from data import y0, y_reverse


def get_polynomial(xi, y):
    polynomial = []

    for i in range(len(xi)):
        coefficients = xi[:i]
        polynomial.append(coefficients)
        diff = get_diff(y, *xi[:(i + 1)])
        polynomial.append(diff)
    return polynomial


def take_x(brackets, x):
    if not brackets:
        return 1
    result = 1
    for bracket in brackets:
        result *= (x - bracket)
    return result


def count_value(polynomial, x):
    result = 0
    for i in range(0, len(polynomial), 2):
        result += take_x(polynomial[i], x) * polynomial[i + 1]
    return result


def main():
    start = 0.00
    finish = 1.05
    step = 0.15
    try:
        x = float(input('Введите x: '))
    except ValueError:
        return print('Вы должны ввести число')

    print('\n|', '-' * 7, '|', '-' * 14, '|', '-' * 14, '|', '-' * 14, '|', sep='')
    print('|Степень| Для полинома | Для полинома | Для обратной |')
    print('|       |    Ньютона   |     Эрмита   | интерполяции |')
    for n in range(1, 5):
        print('|', '-' * 7, '|', '-' * 14, '|', '-' * 14, '|', '-' * 14, '|', sep='')

        xi_newton = get_xi_newton(n, x, start, finish, step)
        polynomial_newton = get_polynomial(xi_newton, y0)
        print(f'|   {n}   |    {count_value(polynomial_newton, x):.6f}', end='  ')

        xi_hermit = get_xi_hermit(n, x, start, finish, step)
        polynomial_hermit = get_polynomial(xi_hermit, y0)
        print(f'|    {count_value(polynomial_hermit, x):.6f}', end='  ')

        xi_reverse = get_xi_reverse(n)
        polynomial_reverse = get_polynomial(xi_reverse, y_reverse)
        print(f'|    {count_value(polynomial_reverse, 0):.6f}  |')

    print('|', '-' * 7, '|', '-' * 14, '|', '-' * 14, '|', '-' * 14, '|', sep='')


if __name__ == '__main__':
    main()
