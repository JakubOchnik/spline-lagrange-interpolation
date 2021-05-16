import matplotlib.pyplot as plt

def plot_points(data, name):

    x = []
    y = []
    for point in data:
        x.append(float(point[0]))
        y.append(float(point[1]))

    plt.plot(x, y)
    plt.title(name)
    plt.ylabel('Height')
    plt.xlabel('Distance')
    plt.show()

def plot_interpolation(data, name, interpolated_y, type="semilogy"):
    x = []
    y = []
    for point in data[1:]:
        x.append(float(point[0]))
        y.append(float(point[1]))

    if type == "semilogy":
        plt.semilogy(x, y)
        plt.semilogy(x, interpolated_y)
    elif type == "regular":
        plt.plot(x, y)
        plt.plot(x, interpolated_y)
    plt.title(name)
    plt.ylabel('Height')
    plt.xlabel('Distance')
    plt.show()