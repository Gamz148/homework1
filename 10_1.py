class Matrix():

    def __init__(self, lst):
        if self.__is_init_data_valid(lst):
            self.data = lst
        else:
            raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")


    def __is_init_data_valid(self, data):
        set_lenghts = {len(lst) for lst in data}
        if len(set_lenghts) == 1:
            return True
        else:
            return False

    @property
    def dim(self):
        return len(self.data), len(self.data[0])

    def __str__(self):
        rez = ""
        for row in self.data:
            rez += "| "
            for element in row:
                rez += f"{element:3d} "
            rez += "|\n"
        return rez

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Incorrect dimensions for add method")
        new_list = []
        for idx, row in enumerate(self.data):
            new_row = []
            for jdx, el in enumerate(row):
                new_row.append(self.data[idx][jdx] + other.data[idx][jdx] )
            new_list.append(new_row)
        return Matrix(new_list)

m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
m3 = Matrix([[1,1],[1,1],[1,1]])
m4 = m1 + m2
print(m4)
m5 = m1 + m3

print(m5)

m3 = Matrix([[1,1,1,1],[1,1,1],[1,1,1]])