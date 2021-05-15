from matrix_handling import *


class SplineInterpolation:
    def __init__(self, data):
        self.n = len(data)
        self.data = data

    def interpolate(self, xp, new_n, interpolation_data):
        y_result = 0
        xp = float(xp)

        print(y_result)
        return y_result

    def pivoting(self):
        pass

    def get_parameters(self, n, data):

        x = []
        y = []
        for point in data[1:]:
            x.append(float(point[0]))
            y.append(float(point[1]))

        A = []
        for i in range(4*(n-1)):
            A.append([0]*(4*(n-1)))

        b = [0] * (4*(n-1))
        
        # conditions startup

        # 1. Sj(xj) = f(xj)
        A[0][0] = 1
        b[0] = y[0]

        # 2. Sj(xj+1) = f(xj+1)
        h = x[1] - x[0]
        A[1][0] = 1
        A[1][1] = h
        A[1][2] = h ** 2
        A[1][3] = h ** 3
        b[1] = y[1]

        # border conditions
        # S_0 '' (x_0) = 0
        A[2][2] = 1
        b[2] = 0

        # S_n-1 '' (x_n) = 0
        h = y[len(y) - 1] - y[len(y) - 2]
        A[3][4*(len(y)-2)+2] = 2
        A[3][4*(len(y)-2)+3] = 6*h
        b[3] = 0

        for i in range(1, n-1):
            h = x[i] - x[i-1]

            # 1. Sj(xj) = f(xj)
        
            A[4 * i][4*i] = 1
            b[4*i] = y[i]
        
            # 2. Sj(xj+1) = f(xj+1)
            A[4*i + 1][4*i] = 1
            A[4*i + 1][4*i + 1] = h
            A[4*i + 1][4*i + 2] = h ** 2
            A[4*i + 1][4*i + 3] = h ** 3
            b[4 * i + 1] = y[i]
        
            # 3. poj pochodna
            A[4*i + 2][4*(i - 1) + 1] = 0 # b0
            A[4*i + 2][4*(i - 1) + 2] = 2 * h # c0
            A[4*i + 2][4*(i - 1) + 3] = 3 * h ** 2 # d0
            A[4*i + 2][4* i + 1] = -1 # b1
            b[4 * i + 2] = 0

            # 4. podw. pochodna
            A[4* i + 3][4*(i-1) + 2] = 2 # 2 c0
            A[4* i + 3][4*(i-1) + 3] = 6 * h # 6h d0
            A[4* i + 3][4*i + 2] = -2 # c1
            b[4*i + 3] = 0
        
        print(A)
        return A, b

    def interpolate_function(self, k):

        interpolation_data = self.data[0::k]
        interpolated_y = []

        A, b = self.get_parameters(len(interpolation_data), interpolation_data)

        '''
        for point in self.data[:-1]:
            x, y = point
            interpolated_y.append(self.interpolate(
                float(x), len(interpolation_data), interpolation_data))

        return interpolated_y
        '''
