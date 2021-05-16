import csv


def load_file(path):
    with open(path, 'r') as f:
        data = list(csv.reader(f))
        if (isinstance(data[0][0], str)):
            data = data[1:]
        for i in range(len(data)):
            x, y = data[i]
            data[i] = [float(x), float(y)]
        return data
