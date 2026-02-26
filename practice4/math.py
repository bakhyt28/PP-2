#1
import math

sides_count = int(input())     # number of sides of the polygon
side_length = int(input())     # length of one side

# calculate the area of a regular polygon using formula:
# Area = (n * a^2) / (4 * tan(pi/n))
polygon_area = int((sides_count * pow(side_length, 2)) /
                   (4 * math.tan(math.pi / sides_count)))

# print the calculated area
print(polygon_area)

#2
import math

angle_degree = float(input())   # read angle value in degrees

# convert degrees to radians using formula:
# radians = degrees * pi / 180
angle_radian = angle_degree * math.pi / 180

# print result with 6 decimal places
print(f"{angle_radian:.6f}")