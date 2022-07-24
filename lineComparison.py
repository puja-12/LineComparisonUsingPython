import math

print("Please Enter x1 and y1 coordinates : ")
x1 = float(input())
y1 = float(input())
print("Please Enter x2 and y2 coordinates : ")
x2 = float(input())
y2 = float(input())

Distance1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("distance between", (x1, x2), "and", (y1, y2), "is : ", Distance1)

print("Please Enter p1 and q1 coordinates ")
p1 = float(input())
q1 = float(input())
print("Please Enter p2 and q2 coordinates ")
p2 = float(input())
q2 = float(input())
Distance2 = math.sqrt((p1 - p2) ** 2 + (q1 - q2) ** 2)
print("distance between", (p1, p2), "and", (q1, q2), "is : ", Distance2)
if Distance1 == Distance2:

    print("{0} is equal to {1}", Distance1, Distance2)
else:
    print("{0} is not equal to {1}", Distance1, Distance2)
