class SplineInterpolation:
    def __init__(self, data):
        self.n = len(data)
        self.data = data
    
    def interpolate(self, xp, new_n, interpolation_data):
        y_result = 0
        xp = float(xp)
        for i in range(new_n):
            #
            p = 1.0
            xi, yi = interpolation_data[i]
            for j in range(new_n):
                if not i == j:
                    xj, yj = interpolation_data[j]
                    p *= (xp - float(xj))/(float(xi) - float(xj))
                else:
                    continue
            y_result += p * float(yi)
        print(y_result)
        return y_result
    
    def interpolate_function(self, k):

        interpolation_data = self.data[1::k]
        interpolated_y = []

        for point in self.data[1:]:
            x, y = point
            interpolated_y.append(self.interpolate(float(x), len(interpolation_data), interpolation_data))

        return interpolated_y
