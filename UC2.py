import math

print("Welcome to Line Comparison Computation Program ")


# Length of line

def Distance(x1, x2, y1, y2):
    finalResult = Distance(x1, x2, y1, y2)
    print("Distance between {0},{1} and {2},{3} is {4:F}", x1, y1, x2, y2, finalResult)

    temp1 = (x2 - x1) ** 2
    temp2 = (y2 - y1) ** 2
    result = math.sqrt(temp1 + temp2)
    return result


if __name__ == "__main__":
    print("Please Enter x1 and y1 coordinates : ")
    x1 = float(input())
    y1 = float(input())
    print("Please Enter x2 and y2 coordinates : ")
    x2 = float(input())
    y2 = float(input())
    Distance(x1, x2, y1, y2)
