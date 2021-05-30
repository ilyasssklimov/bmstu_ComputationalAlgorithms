from data import y0, y_diff


def get_diff(y, *args):
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return y[args[0]]
    elif len(args) == 2 and len(args) != len(set(args)):
        return y_diff[args[0]]
    else:
        return (get_diff(y, *args[:-1]) - get_diff(y, *args[1:])) / (args[0] - args[-1])


def get_xi_newton(n, x, start, finish, step):
    if n < 0:
        raise ValueError('n сan\'t be negative')

    if n > len(y0):
        raise ValueError(f'n сan\'t be more than {len(y0)}')

    array_x = []
    first_element = -1
    for value, i in y0.items():
        if value <= x:
            first_element = value
    array_x.append(first_element)
    inc = 1
    dec = 1

    for _ in range(1, n // 2 + 1):
        value_up = round(first_element + inc * step, 2)
        value_down = round(first_element - dec * step, 2)
        if value_up <= finish:
            array_x.append(value_up)
            inc += 1
        else:
            array_x.append(value_down)
            dec += 1

        value_down = round(first_element - dec * step, 2)
        value_up = round(first_element + inc * step, 2)
        if value_down >= start:
            array_x.append(value_down)
            dec += 1
        else:
            array_x.append(value_up)
            inc += 1

    if n % 2 != 0:
        value_up = round(first_element + inc * step, 2)
        value_down = round(first_element - dec * step, 2)
        if value_up <= finish:
            array_x.append(value_up)
        else:
            array_x.append(value_down)

    return sorted(array_x)


def get_xi_hermit(n, x, start, finish, step):
    if n < 0:
        raise ValueError('n сan\'t be negative')

    if n > len(y0):
        raise ValueError(f'n сan\'t be more than {len(y0)}')

    array_x = []
    xi_newton = get_xi_newton(n // 2, x, start, finish, step)
    for x in xi_newton:
        array_x.append(x)
        array_x.append(x)
    array_x = array_x[:(n + 1)]
    return array_x


def get_xi_reverse(n):
    if n < 0:
        raise ValueError('n сan\'t be negative')

    if n > len(y0):
        raise ValueError(f'n сan\'t be more than {len(y0)}')

    values = list(y0.values())
    first_index = 4
    first_element = values[first_index]
    array_x = [first_element]
    array_x.extend(values[(first_index - n // 2):first_index])
    array_x.extend(values[(first_index + 1):(first_index + n // 2) + 1])
    if n % 2 != 0:
        array_x.append(values[first_index + n // 2 + 1])

    return sorted(array_x)
