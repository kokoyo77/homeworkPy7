def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(f"{result:4}", end=" ")
        print()

# Пример использования функции с операцией умножения
def multiplication(row, col):
    return row * col

# Вывод таблицы умножения размером 6x6
print_operation_table(multiplication)
