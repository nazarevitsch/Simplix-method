from enum import Enum


class MinMax(Enum):
    NONE = 0
    MIN = 1
    MAX = 2


class Table:
    table = [[]]
    metadata_row = []
    metadata_column = []
    min_max = MinMax.NONE

    def __init__(self, table, metadata_row, metadata_column, min_max):
        self.table = table
        self.metadata_row = metadata_row
        self.metadata_column = metadata_column
        self.min_max = min_max
        self.prove()

    def prove(self):
        if len(self.table) != len(self.metadata_column):
           raise Exception('Len of metadata column and rows len in matrix are unequal!')
        for i in self.table:
            if len(i) != len(self.metadata_row):
                raise Exception('Len of metadata row and len of row in matrix are unequal!')

    def clone(self):
        table = []
        i = 0
        while i < len(self.table):
            table.append(self.table[i].copy())
            i += 1
        metadata_row = self.metadata_row.copy()
        metadata_column = self.metadata_column.copy()
        return Table(table, metadata_row, metadata_column, self.min_max)

    def print(self, title):
        print("Table: " + title + "\n_" + "_________" * (len(self.metadata_row) + 1))
        print("|        |", end='')
        i = 0
        while i < len(self.metadata_row):
            print(self.metadata_row[i] + ' ' * (8 - len(self.metadata_row[i])) + '|', end='')
            i += 1
        print()
        print("_" + "_________" * (len(self.metadata_row) + 1))
        i = 0
        while i < len(self.table):
            l = 0
            print('|' + self.metadata_column[i] + ' ' * (8 - len(self.metadata_column[i])) + '|', end='')
            while l < len(self.table[i]):
                print(str(round(self.table[i][l], 5)) + ' ' * (8 - len(str(round(self.table[i][l], 5)))) + '|', end='')
                l += 1
            print()
            print("_" + "_________" * (len(self.metadata_row) + 1))
            i += 1