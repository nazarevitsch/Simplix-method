class Table:
    table = [[]]
    metadata_row = []
    metadata_column = []


    def __init__(self, table, metadata_row, metadata_column):
        self.table = table
        self.metadata_row = metadata_row
        self.metadata_column = metadata_column


    def clone(self):
        table = []
        i = 0
        while i < len(self.table):
            table.append(self.table[i].copy())
            i += 1
        metadata_row = self.metadata_row.copy()
        metadata_column = self.metadata_column.copy()
        return Table(table, metadata_row, metadata_column)


    def print(self):
        print("Table:\n_" + "_________" * (len(self.metadata_row) + 1))
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