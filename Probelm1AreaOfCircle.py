# Leslie Bacajol
# 11/09/21
# Problem 1
# This function returns the area of a circle of radius r

import math

def areaofcircle(r):
    area = math.pi * r * r
    return area

radius = 5
print("Area", round(areaofcircle(radius), 2))
