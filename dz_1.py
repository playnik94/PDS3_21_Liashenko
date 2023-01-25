class Matrix():

    def __init__(self, A, B, C, number, X, transpose):
        self.A = A
        self.B = B
        self.C = C
        self.number = number
        self.X = X
        self.transpose = transpose

    def plus(self):
        for x in range(len(self.A)):
            for i in range(len(self.A[0])):
                self.C[x][i] = self.A[x][i] + self.B[x][i]

        for t in self.C:
            print(t)

    def minus(self):
       for o in range(len(self.A)):
           for k in range(len(self.A[0])):
               self.C[o][k] = self.A[o][k] - self.B[o][k]

       for r in self.C:
           print(r)

    def multiplication(self):
        for q in range(len(self.A)):
            for y in range(len(self.B[0])):
                for p in range(len(self.B)):
                    self.C[q][y] += self.A[q][p] * self.B[q][y]

        for h in self.C:
            print(h)

    def multipi_on_number(self):
        for o in range(len(self.A)):
            for u in range(len(self.A[0])):
                self.C[o][u] = self.A[o][u] * self.number

        for j in self.C:
            print(j)

    def Transpose(self):
        for g in range(len(self.X)):
            for j in range(len(self.X[0])):
                self.transpose[j][g] = self.X[g][j]
        for z in self.transpose:
            print(z)

    def exeption(self):
        for a in range(len(self.X)):
            for s in range(len(self.X)):
                self.C[s][a] = self.X[a][s]
        for d in self.C:
            print(d)


root = Matrix([[12, 7, 3],
               [4, 5, 6],
               [7, 8, 9]],

              [[5, 8, 1],
               [6, 7, 3],
               [4, 5, 9]],

              [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]],

                  8,

              [[12, 7],
                [4, 5],
                [3, 8]],

              [[0, 0, 0],
               [0, 0, 0]])



print('Plus')
root.plus()
print('\n')
print('Minus')
root.minus()
print('\n')
print('Multiplication')
root.multiplication()
print('\n')
print('Multipilication on number')
root.multipi_on_number()
print('\n')
print('Transpose')
root.Transpose()
print('\n')
print('exeption')
try:
    root.exeption()
except IndexError as ex:
    print(f'Кол.во строк должны быть равным кол.во столбиков: {ex}')
