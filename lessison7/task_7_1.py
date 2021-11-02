class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list
        n = len(self.my_list[0])
        for line in self.my_list:
            if len(line) != n:
                raise ValueError("Не верный формат данных")

    def __str__(self):
        s = ""
        for row in self.my_list:
            line = ""
            for el in row:
                line = line + str(el) + " "
            s = s + line + "\n"
        return s

    def __add__(self, other):
        if len(self.my_list) != len(other.my_list):
            raise ValueError("Матрицы разные")
        new_matrix = list()
        new_line = list()
        i = 0
        j = 0
        for line1 in self.my_list:
            line2 = other.my_list[j]
            for el in line1:
                new_line.append(el+line2[i])
                i += 1
            j += 1
            i = 0
            new_matrix.append(new_line)
            new_line = list()
        return Matrix(new_matrix)


m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m2 = [[11, 2, 3, 4], [5, 6, 77, 8], [9, 10, 11, 12]]
matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
print(matrix1+matrix2)


