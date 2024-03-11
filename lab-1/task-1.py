import math

x1 = int(input("Enter x1="))
y1 = int(input("Enter y1="))

x2 = int(input("Enter x2="))
y2 = int(input("Enter y2="))


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2))


result = euclidean_distance(x1, y1, x2, y2)

print(result)
