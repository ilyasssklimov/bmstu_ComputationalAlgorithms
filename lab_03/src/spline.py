def create_spline(x_table, y_table):
    n = len(x_table)
    splines = [{'x': x_table[i], 'a': y_table[i], 'b': 0, 'c': 0, 'd': 0} for i in range(n)]
    splines[0]['c'], splines[-1]['c'] = 0.0, 0.0

    alpha = [0.0 for _ in range(n - 1)]
    beta = [0.0 for _ in range(n - 1)]

    for i in range(n - 2):
        h1 = x_table[i + 1] - x_table[i]
        h2 = x_table[i + 2] - x_table[i + 1]

        a = h1
        b = h2
        c = 2.0 * (h1 + h2)

        f = (y_table[i + 2] - y_table[i + 1]) / h2 - (y_table[i + 1] - y_table[i]) / h1
        f *= 6.0

        t = a * alpha[i] + c
        alpha[i + 1] = -b / t
        beta[i + 1] = (f - a * beta[i]) / t

    for i in range(n - 2, 0, -1):
        splines[i]['c'] = alpha[i] * splines[i + 1]['c'] + beta[i]

    for i in range(n - 1, 0, -1):
        h = x_table[i] - x_table[i - 1]
        splines[i]['d'] = (splines[i]['c'] - splines[i - 1]['c']) / h
        splines[i]['b'] = h * (2.0 * splines[i]['c'] + splines[i - 1]['c']) / 6.0
        splines[i]['b'] += (y_table[i] - y_table[i - 1]) / h

    return splines


def interpolation_spline(splines, x):
    if not splines:
        raise ValueError('First param is empty')

    n = len(splines)

    if x <= splines[0]['x']:
        spline = splines[0]
    elif x >= splines[-1]['x']:
        spline = splines[-1]
    else:
        left, right = 0, n - 1
        while left + 1 < right:
            m = left + (right - left) // 2
            if x <= splines[m]['x']:
                right = m
            else:
                left = m
        spline = splines[right]

    dx = x - spline['x']

    result = spline['a'] + (spline['b'] + (spline['c'] / 2.0 + spline['d'] * dx / 6.0) * dx) * dx
    return result
