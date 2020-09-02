""" In order to test our Random Number generator, we use a simple Monte Carlo method to test it
Consider a square and its inscribed circle in a 2-D rectangular coordinate. The length of square 
and the diameter of the circle are 2, and the center of them are both origin of this coordinate.
The number of points in the circle vs. in square will give us an estimate of ratio of area between inscribed
circle and its square"""


from point import Point, PointCollection
from generator import LCG, SCG

class MCTestLCG:
    def __init__(self):
        self.points = PointCollection()
        self.lcg = LCG(1, 1103515245, 2 ** 32, 12345678)
        for i in range(0, 10000000):
            x = self.lcg.next_random_number()
            y = self.lcg.next_random_number()
            self.points.addPoint(Point(self.normalize(x), self.normalize(y)))

    def testRatio(self):
        withinCircle = 0
        for point in self.points.getCollection():
            if (point.distance() <= 1):
                withinCircle += 1
        return withinCircle/self.points.getCollection().__len__()

    def normalize(self, toNormalize):
        return (toNormalize - 0.5)*2


class MCTestSCG:
    def __init__(self):
        self.points = PointCollection()
        self.lcg = SCG(6, 1103515245, 2 ** 32, 12345678)
        for i in range(0, 10000000):
            x = self.lcg.next_random_number()
            y = self.lcg.next_random_number()
            self.points.addPoint(Point(self.normalize(x), self.normalize(y)))

    def testRatio(self):
        withinCircle = 0
        for point in self.points.getCollection():
            if (point.distance() <= 1):
                withinCircle += 1
        return withinCircle/self.points.getCollection().__len__()

    def normalize(self, toNormalize):
        return (toNormalize - 0.5)*2

# testing the ratio
print("Test ratio LCG: " + str(MCTestLCG().testRatio()))
print("Test ration SCG: " + str(MCTestSCG().testRatio()))
