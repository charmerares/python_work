# import sys
#
# sys.path.append("E:\\code\\python\\python_work\\main")
from test.testCar import testCar
from bike import testBike as Bike

if __name__ == "__main__":
    car = testCar()
    car.test()
    Bike()


def test():
    print("hello world")
