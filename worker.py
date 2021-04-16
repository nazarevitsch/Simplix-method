from table import *
from sys import *


def calculate(table):
    index_z_row = find_index_of_z(table)
    result_index_column = find_index_of_result(table)

    iterations = 0
    while not check(table, index_z_row):
        print('Begin: ' + str(iterations))
        table.print()
        min_index_in_z_column = find_index_of_min_number_in_z(table, index_z_row)
        index_min_result_row = find_min_index_in_result(table, result_index_column, index_z_row, min_index_in_z_column)
        table.metadata_column[index_min_result_row] = table.metadata_row[min_index_in_z_column]
        # table.print()
        divide_row(table, index_min_result_row, min_index_in_z_column, result_index_column)
        # table.print()
        table = switch_after_dividing(table, index_min_result_row, min_index_in_z_column, result_index_column)
        print('Finish: ' + str(iterations))
        table.print()
        iterations += 1


def check(table, index_z_row):
    for i in table.table[index_z_row]:
        if i < 0:
            return False
    return True


def switch_after_dividing(table, index_min_result_row, min_index_in_z_column,  result_index_column):
    new_table = table.clone()
    i = 0
    while i < len(table.table[index_min_result_row]):
        if table.table[index_min_result_row][i] == 1 and i != result_index_column:
            l = 0
            while l < len(table.table):
                if index_min_result_row != l:
                    new_table.table[l][i] = 0
                l += 1
        elif table.table[index_min_result_row][i] != 0:
            l = 0
            while l < len(table.table):
                if index_min_result_row != l:
                    new_table.table[l][i] = ((table.table[l][i] * table.table[index_min_result_row][min_index_in_z_column]) - (table.table[index_min_result_row][i] * table.table[l][min_index_in_z_column])) / table.table[index_min_result_row][min_index_in_z_column]
                l += 1
        i += 1
    return new_table


def divide_row(table, index_min_result_row, min_index_in_z_column, result_index_column):
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


def dividing_of_result(table, index_z, result_index, min_index_in_z):
    i = 0
    while i < len(table.table):
        if i != index_z:
            table.table[i][result_index] /= table.table[i][min_index_in_z]
        i += 1


def find_index_of_result(table):
    l = 0
    while l < len(table.metadata_row):
        if table.metadata_row[l] == 'Res':
            return l
        l += 1
    return -1


def find_index_of_min_number_in_z(table, index_z):
    i = 0
    index = -1
    number = table.table[index_z][0]
    while i < len(table.table[index_z]):
        if number >= table.table[index_z][i]:
            number = table.table[index_z][i]
            index = i
        i += 1
    return index


def find_index_of_z(table):
    i = 0
    while i < len(table.metadata_column):
        if table.metadata_column[i] == 'Z':
            return i
        i += 1
    return -1