from math import sqrt


def main():
    print("Welcome to Line Comparison Computation Program ")

    print("Please Enter x1 and y1 coordinates : ")
    x1 = float(input())
    y1 = float(input())
    print("Please Enter x2 and y2 coordinates : ")
    x2 = float(input())
    y2 = float(input())

    Distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    print("distance between", (x1, x2), "and", (y1, y2), "is : ", Distance)

    return Distance


if __name__ == "__main__":
    main()
