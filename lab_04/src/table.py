def print_table(table):
    def separator():
        print('|', '-' * 9, '|', '-' * 9, '|', '-' * 9, '|', sep='')

    print('Исходная таблица:')
    separator()
    print('|    x    |    y    |   Вес   |')
    separator()
    for line in table:
        print(f'|{str(line[0]):^9s}|{str(line[1]):^9s}|{str(line[2]):^9s}|')
        separator()
    print()


def create_table(filename):
    with open(f'data/{filename}') as f:
        table = [tuple(map(float, line.split())) for line in f if line]

    return table
