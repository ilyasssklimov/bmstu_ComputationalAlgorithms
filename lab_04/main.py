from bmstu_ComputationalAlgorithms.lab_04.find import find_coefficients
from bmstu_ComputationalAlgorithms.lab_04.show import show_result
from bmstu_ComputationalAlgorithms.lab_04.table import create_table, print_table


def main():
    filename = '1.txt'
    print(f'Результат на основе данных файла data/{filename}\n')
    table = create_table(filename)
    print_table(table)

    try:
        degree = int(input('Введите степень полинома: '))
    except ValueError:
        return print('Ошибка! Вы должны были ввести число')

    result = find_coefficients(table, degree)
    print('\nРезультат можно увидеть на появившемся графике')
    show_result(table, result, degree)


if __name__ == '__main__':
    main()
