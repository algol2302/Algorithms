"""Design a parking system for a parking lot. The parking lot has three kinds
of parking spaces: big, medium, and small, with a fixed number of slots for
each size.

Implement the ParkingSystem class:

* ParkingSystem(int big, int medium, int small) Initializes object of the
ParkingSystem class. The number of slots for each parking space are given as
part of the constructor.
* bool addCar(int carType) Checks whether there is a parking space of carType
for the car that wants to get into the parking lot. carType can be of three
kinds: big, medium, or small, which are represented by 1, 2, and 3
respectively. A car can only park in a parking space of its carType. If there
is no space available, return false, else park the car in that size space and
return true.

Input:
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output:
[null, true, true, false, false]
"""


class ParkingSystem:
    __slots__ = ["places"]

    def __init__(self, big: int, medium: int, small: int):
        self.places = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.places[carType]:
            self.places[carType] -= 1
            return True
        return False


def main():
    obj = ParkingSystem(1, 1, 0)
    assert obj.addCar(1) == True
    assert obj.addCar(2) == True
    assert obj.addCar(3) == False
    assert obj.addCar(1) == False

    obj = ParkingSystem(0, 0, 2)
    assert obj.addCar(1) == False
    assert obj.addCar(2) == False
    assert obj.addCar(3) == True


if __name__ == "__main__":
    main()
