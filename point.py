
""" Class to represent the points in rectangular coordinate """


from math import sqrt

class Point():
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def distance(self):
        return sqrt(self.x_coordinate**2  + self.y_coordinate**2)

class PointCollection():
    def __init__(self):
        self.collection = []

    def addPoint(self, point):
        self.collection.append(point)

    def getCollection(self):
        return self.collection