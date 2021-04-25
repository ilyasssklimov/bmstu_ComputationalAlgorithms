import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def show_result(table, result, degree):
    matplotlib.use('TkAgg')
    if len(table) > 1:
        dx = table[1][0] - table[0][0]
    else:
        dx = 10

    x = np.linspace(table[0][0] - dx, table[-1][0] + dx, 100)
    y = []
    for xi in x:
        tmp = 0
        for i in range(degree + 1):
            tmp += xi ** i * result[i]
        y.append(tmp)
    plt.plot(x, y)

    y_min, y_max = min(y), max(y)

    x = [point[0] for point in table]
    y = [point[1] for point in table]
    plt.plot(x, y, 'o', color='red', label='Исходные точки')
    plt.legend(loc='best')

    y_min, y_max = min(y_min, min(y)), max(y_max, max(y))
    dy = (y_max - y_min) * 0.03

    plt.axis([table[0][0] - dx, table[-1][0] + dx, y_min - dy, y_max + dy])
    plt.show()
