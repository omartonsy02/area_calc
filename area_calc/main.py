# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def area():

    # Use a breakpoint in the code line below to debug your script.
    print("which area you want to calculate \n 1-Circle \n 2-rect \n 3-square \n 4-triangle")
    num = int(input())
    if num == 1:
        r = int(input("Enter r:"))
        ar = math.pi * r * r
    elif num == 2:
        e = int(input("Enter edge length:"))
        ar = e * e
    elif num == 3:
        l = int(input("Enter length:"))
        w = int(input("Enter width:"))
        ar = l * w
    elif num == 4:
        b = int(input("Enter Base length:"))
        l = int(input("Enter length:"))
        ar = b * l / 2
    else:
        print("error please try again \n")
        area()

    return ar


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(area())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
