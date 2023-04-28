"""
计算两点之间的距离
1. 使用_表示私有属性，并且使用访问器和修改器
2. 使用了__slots__ 属性对私有属性和方法进行限制
3. 使用静态方法@staticmethod 限制点位范围
"""
from math import sqrt

class Point :
    __slots__ = ("_x","_y")
    def __init__(self,x,y):
        self._x = x
        self._y = y

    @staticmethod
    def isint(x,y):
        return -10 < x <10 and -10< y <10
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self,x):
        self._x = x
    @y.setter
    def y(self,y):
        self._y = y

    def distance (self,other):
        xt = self.x - other.x
        yt = self.y - other.y
        return sqrt(yt ** 2 + xt ** 2)

def main():
    if Point.isint(1,9) and Point(2,5):
        p1 = Point(1,4)
        p2 = Point(2,5)
    print(p1.distance(p2))


if __name__ == "__main__":
    main()




