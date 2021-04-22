from worker import *
from table import *


if __name__ == '__main__':
    # t = [[-3, -2, 0, 0, 0], [-5, 2, 1, 0, 12], [8, 3, 0, 1, 80]]
    # md1 = ['X1', 'X2', 'S1', 'S2', 'Res']
    # md2 = ['Z', 'S1', 'S2']
    # table = Table(t, md1, md2)

    # t = [[-4, -5, 0, 0, 0, 0], [-1, 1, 1, 0, 0, 4], [1, 2, 0, 1, 0, 2], [3, 2, 0, 0, 1, 6]]
    # md1 = ['X1', 'X2', 'S1', 'S2', 'S3', 'Res']
    # md2 = ['Z', 'S1', 'S2', 'S3']
    # table = Table(t, md1, md2)
    # calculate_one_step(table)

    # t = [[2, 1, 0, 0, -1, -1, 0, 0, 10], [-3, -2, 0, 0, 0, 0, 0, 0, 0], [-5, 2, 1, 0, 0, 0, 0, 0, 12],
    #      [8, 3, 0, 1, 0, 0, 0, 0, 80], [1, 1, 0, 0, -1, 0, 1, 0, 8], [1, 0, 0, 0, 0, -1, 0, 1, 2]]
    # md1 = ['X1', 'X2', 'S1', 'S2', 'S3', 'S4', 'R1', 'R2', 'Res']
    # md2 = ['R', 'Z', 'S1', 'S2', 'R1', 'R2']
    # table = Table(t, md1, md2, MinMax.MIN)
    # calculate_two_steps(table)

    t = [[8, 3, 0, -1, 0, 80],
         [-3, -2, 0, 0, 0, 0],
         [-5, 2, 1, 0, 0, 12],
         [8, 3, 0, -1, 1, 80]]
    md1 = ['X1', 'X2', 'S1', 'S2', 'R1', 'Res']
    md2 = ['R', 'Z', 'S1', 'S2', 'R1']
    table = Table(t, md1, md2, MinMax.MIN)
    calculate_two_steps(table)

