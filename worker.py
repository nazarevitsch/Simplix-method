from table import *
from sys import *


def calculate_two_steps(table):
    result_index_column = find_row_index_of_result(table)
    index_r_row = find_index_of_row_by_letter(table, 'R')

    table.print()
    print("\n\nStart of First Step\n\n")
    while not check(table, index_r_row):
        min_max_index_in_r_column = find_min_max_index_in_column(table, index_r_row, result_index_column)
        index_min_result_row = find_min_index_in_result(table, result_index_column, index_r_row, min_max_index_in_r_column)
        table.metadata_column[index_min_result_row] = table.metadata_row[min_max_index_in_r_column]
        divide_row(table, index_min_result_row, min_max_index_in_r_column)
        table = switch_after_dividing(table, index_min_result_row, min_max_index_in_r_column)
        table.print()
    table = prepare_table(table)
    print("\n\nStart of Second Step\n\n")
    calculate_one_step(table)


def calculate_one_step(table):
    index_z_row = find_index_of_row_by_letter(table, 'Z')
    result_index_column = find_row_index_of_result(table)

    while not check(table, index_z_row):
        min_index_in_z_column = find_min_max_index_in_column(table, index_z_row, result_index_column)
        index_min_result_row = find_min_index_in_result(table, result_index_column, index_z_row, min_index_in_z_column)
        table.metadata_column[index_min_result_row] = table.metadata_row[min_index_in_z_column]
        divide_row(table, index_min_result_row, min_index_in_z_column)
        table = switch_after_dividing(table, index_min_result_row, min_index_in_z_column)
        table.print()


def prepare_table(table):
    i = len(table.metadata_column) - 1
    while i >= 0:
        if 'R' in table.metadata_column[i]:
            table.table.pop(i)
            table.metadata_column.pop(i)
        i -= 1
    i = len(table.metadata_row) - 1
    while i >= 0:
        if 'R' in table.metadata_row[i] and table.metadata_row[i] != 'Res':
            l = 0
            while l < len(table.table):
                table.table[l].pop(i)
                l += 1
            table.metadata_row.pop(i)
        i -= 1
    table.min_max = MinMax.MAX
    return table


def check(table, row_index):
    for i in table.table[row_index]:
        if table.min_max == MinMax.MAX:
            if i < 0:
                return False
        elif table.min_max == MinMax.MIN:
            if i > 0:
                return False
    return True


def switch_after_dividing(table, index_min_result_row, min_index_in_z_column):
    new_table = table.clone()
    i = 0
    while i < len(table.metadata_row):
        l = 0
        flag = True
        while l < len(table.metadata_column):
            if table.metadata_row[i] == table.metadata_column[l]:
                if l == index_min_result_row:
                    j = 0
                    while j < len(table.table):
                        if j != index_min_result_row:
                            new_table.table[j][i] = 0
                        j += 1
                else:
                    j = 0
                    while j < len(table.table):
                        new_table.table[j][i] = table.table[j][i]
                        j += 1
                flag = False
                break
            l += 1
        if flag:
            l = 0
            while l < len(table.table):
                if index_min_result_row != l:
                    new_table.table[l][i] = ((table.table[l][i] * table.table[index_min_result_row][min_index_in_z_column]) - (table.table[index_min_result_row][i] * table.table[l][min_index_in_z_column])) / table.table[index_min_result_row][min_index_in_z_column]
                l += 1
        i += 1
    return new_table


def divide_row(table, index_min_result_row, min_index_in_z_column):
    i = 0
    divider = table.table[index_min_result_row][min_index_in_z_column]
    while i < len(table.table[index_min_result_row]):
        table.table[index_min_result_row][i] /= divider
        i += 1


def find_min_index_in_result(table, result_index_column, index_z_row, min_index_in_z):
    i = 0
    index = -1
    number = maxsize
    while i < len(table.table):
        if index_z_row != i and (table.table[i][result_index_column] / table.table[i][min_index_in_z] > 0) and ((table.table[i][result_index_column] / table.table[i][min_index_in_z]) < number):
            number = table.table[i][result_index_column] / table.table[i][min_index_in_z]
            index = i
        i += 1
    return index


def find_row_index_of_result(table):
    l = 0
    while l < len(table.metadata_row):
        if table.metadata_row[l] == 'Res':
            return l
        l += 1
    return -1


def find_min_max_index_in_column(table, index_column, index_result_column):
    i = 0
    index = -1
    number = table.table[index_column][0]
    while i < len(table.table[index_column]):
        if table.min_max == MinMax.MAX:
            if number >= table.table[index_column][i] and index_result_column != i:
                number = table.table[index_column][i]
                index = i
        else:
            if number <= table.table[index_column][i] and index_result_column != i:
                number = table.table[index_column][i]
                index = i
        i += 1
    return index


def find_index_of_row_by_letter(table, letter):
    i = 0
    while i < len(table.metadata_column):
        if table.metadata_column[i] == letter:
            return i
        i += 1
    return -1

