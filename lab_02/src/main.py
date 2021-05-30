from data import z0


def get_diff(y, *args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return y[args[0]]
    else:
        return (get_diff(y, *args[:-1]) - get_diff(y, *args[1:])) / (args[0] - args[-1])


def get_xi(nx, x):
    if nx < 0 or nx > 4:
        raise ValueError('nx can\'t be more than maximum amount and less then zero')

    first_element = min(range(5), key=lambda value: abs(x - value))  # поиск ближайшего значения к x
    xi_array = [first_element + step for step in range(0, nx // 2 + 2) if first_element + step <= 4]
    xi_array.extend([first_element + step for step in range(-(nx - len(xi_array) + 1), 0) if first_element + step >= 0])
    xi_array.extend([first_element + step + (nx // 2 + 2) for step in range(nx - len(xi_array) + 1)])

    xi_array.sort()
    return xi_array


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
    try:
        x, y = map(float, input('Введите x и y через пробел: ').split())
    except ValueError:
        return print('Вы должны были ввести два числа')

    print(f'\nМногомерная интерполяция при x = {x}, y = {y}')
    print('|', '-' * 11, '|', '-' * 20, '|', sep='')
    print('|  Степень  |  Результат z(x, y) |')
    for nx, ny in zip(range(1, 4), range(1, 4)):
        yi = get_xi(ny, y)
        xi = get_xi(nx, x)
        xi_values = dict()
        for i in yi:
            polynomial = get_polynomial(xi, z0[i])
            xi_values[i] = count_value(polynomial, x)

        polynomial = get_polynomial(yi, xi_values)
        print('|', '-' * 11, '|', '-' * 20, '|', sep='')
        print(f'|     {nx}     |      {count_value(polynomial, y):.6f}      |')
    print('|', '-' * 11, '|', '-' * 20, '|', sep='')


if __name__ == '__main__':
    main()
