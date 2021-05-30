import tkinter as tk


x_init = [1, 2, 3, 4, 5, 6]
y_init = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]


def left_side(y, h, i):
    if i > 0:
        return (y[i] - y[i - 1]) / h
    else:
        return None


def center_side(y, h, i):
    if 0 < i < len(y) - 1:
        return (y[i + 1] - y[i - 1]) / (2 * h)
    else:
        return None


def runge(y, h, i):
    if i > 1:
        return 2 * left_side(y, h, i) - (y[i] - y[i - 2]) / (2 * h)
    else:
        return None


def align_vars(x, y, i):
    if i < len(y) - 1:
        tmp = (1 / y[i + 1] - 1 / y[i]) / (1 / x[i + 1] - 1 / x[i])
        return tmp * y[i] ** 2 / x[i] ** 2
    else:
        return None


def second(y, h, i):
    if 0 < i < len(y) - 1:
        return (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
    else:
        return None


def get_result():
    result = [[x, y] for x, y in zip(x_init, y_init)]
    length = len(x_init)
    methods = [left_side, center_side, runge, align_vars, second]
    for i in range(length):
        for method in methods:
            if method != align_vars:
                value = method(y_init, x_init[1] - x_init[0], i)
            else:
                value = align_vars(x_init, y_init, i)

            result[i].append(value)

    return result


def show_table(table):
    root = tk.Tk()
    rows, columns = len(table), len(table[0])
    names = ['x', 'y', '1', '2', '3', '4', '5']
    for i in range(len(names)):
        tk.Label(root, text=names[i], width=10, font='Times 16',
                 borderwidth=2, relief='ridge').grid(row=0, column=i)

    for i in range(rows):
        tk.Label(root, text=f'{table[i][0]}', width=10, font='Times 16',
                 borderwidth=2, relief='ridge').grid(row=i + 1, column=0)
        for j in range(1, columns):
            tk.Label(root, text=f'{table[i][j]:.3f}' if table[i][j] else '-', width=10, font='Times 16',
                     borderwidth=2, relief='ridge').grid(row=i + 1, column=j)

    root.mainloop()


def main():
    table = get_result()
    show_table(table)


if __name__ == '__main__':
    main()
