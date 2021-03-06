from interpolation.lagrange import LagrangeInterpolation
from interpolation.spline import SplineInterpolation
from utilities.file_handler import load_file
from utilities.visualizer import plot_interpolation, plot_points


FOLDER_NAME = "data/"
FILE_NAME = "sample2.csv"

INTERVALS = 10

if __name__ == "__main__":
    data = load_file(FOLDER_NAME + FILE_NAME)

    plot_points(data, FILE_NAME)

    interpolator = LagrangeInterpolation(data)
    interpolated_points = interpolator.interpolate_function(INTERVALS)
    plot_interpolation(data, FILE_NAME, interpolated_points, type="semilogy")

    interpolator = SplineInterpolation(data)
    interpolated_points = interpolator.interpolate_function(INTERVALS)
    plot_interpolation(data, FILE_NAME, interpolated_points, type='regular')
