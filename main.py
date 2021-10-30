# In PyCharm, create a project named `Exercise_23` with a file named `main.py`. Use this file to do a basic program
# planning and write in the main function the solution to the following exercise.

# Create a program that given a sequence of 3 angles as input classifies which triangle can be built with them:
# Equilateral, Isosceles, Scalene, or None. Then, the program should print out how many of each type can be built.

# Your program should contain the classes:
# `TriangleClassifier`, `Triangle`, `Equilateral`, `Isosceles`, and `Scalene`.

# The input file is given by the file `input.csv` as generated by the following code:
from operator import itemgetter


class Triangle:

    def __init__(self, angle_1, angle_2, angle_3):
        self.angle_1 = angle_1
        self.angle_2 = angle_2
        self.angle_3 = angle_3

    def type(self):
        return 'unknown'


class Equilateral(Triangle):

    def __init__(self, angle):
        super(Equilateral, self).__init__(angle, angle, angle)

    def type(self):
        return 'equilateral'


class Isosceles(Triangle):

    def __init__(self, angle_1, angle_2):
        super(Isosceles, self).__init__(angle_1, angle_2, angle_2)

    def type(self):
        return 'isosceles'


class Scalene(Triangle):

    def type(self):
        return 'scalene'


def is_triangle(angle_1, angle_2, angle_3):
    return angle_1 + angle_2 + angle_3 == 180.0


def is_equilateral(angle_1, angle_2, angle_3):
    return is_triangle(angle_1, angle_2, angle_3) and angle_1 == angle_2 and angle_2 == angle_3


def is_isosceles(angle_1, angle_2, angle_3):
    return is_triangle(angle_1, angle_2, angle_3) and \
           (angle_1 == angle_2 and angle_3 != angle_1) or \
           (angle_2 == angle_3 and angle_1 != angle_2) or \
           (angle_1 == angle_3 and angle_2 != angle_1)


def is_scalene(angle_1, angle_2, angle_3):
    return is_triangle(angle_1, angle_2, angle_3) and \
           angle_1 != angle_2 and angle_1 != angle_3 and angle_2 != angle_3


class TriangleClassifier:

    def __init__(self):
        self.list_of_angles = []

    def classify(self, angle_1, angle_2, angle_3):
        res = None
        if is_equilateral(angle_1, angle_2, angle_3):
            res = Equilateral(angle_1)
        elif is_isosceles(angle_1, angle_2, angle_3):
            if angle_1 == angle_2:
                res = Isosceles(angle_1, angle_3)
            elif angle_1 == angle_3:
                res = Isosceles(angle_1, angle_2)
            else:
                res = Isosceles(angle_2, angle_3)
        elif is_scalene(angle_1, angle_2, angle_3):
            return Scalene(angle_1, angle_2, angle_3)
        return res


def read_csv_of_floats(file):
    res = []
    with open(file, 'r') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [float(item.strip()) for item in items]
            res.append(items)
    return res


def main():
    print('Angles Analyzer (1.0)')

    triangle_classifier = TriangleClassifier()

    # read csv files and create angles
    print('\nReading the input file')
    list_of_angles = read_csv_of_floats('input.csv')
    print(len(list_of_angles), 'triplet of angles read')

    # classify triangles
    print('\nClassify angles of triangles')
    triangles = []
    for i, angles in enumerate(list_of_angles):
        angle_1, angle_2, angle_3 = angles
        triangle = triangle_classifier.classify(angle_1, angle_2, angle_3)
        triangles.append(triangle)
        # if the triangle is not None
        if triangle:
            print(i, '\t', angles, '\t', triangle.type())

    print('\nFrequency of each type:')
    freqs = {None: 0}
    for triangle in triangles:
        if triangle and triangle.type() not in freqs:
            freqs[triangle.type()] = 0
        freqs[triangle.type()] += 1

    for triangle, amount in sorted(freqs.items(), key=itemgetter(1), reverse=True):
        if triangle:
            print(amount, '\t', triangle)
        else:
            print(amount, '\t impossible')

if __name__ == '__main__':
    main()
