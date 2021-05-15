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

    def get_parameters(self):
        pass
    
    def interpolate_function(self, k):

        interpolation_data = self.data[1::k]
        interpolated_y = []

        for point in self.data[1:]:
            x, y = point
            interpolated_y.append(self.interpolate(float(x), len(interpolation_data), interpolation_data))

        return interpolated_y
