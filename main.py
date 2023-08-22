class Example:
    @staticmethod
    def sum(number):
        if number > 0:
            return number + 5
        else:
            return "Отрицательное число либо 0"


f = Example.sum(6)
print(f)


class Follower(Example):
    def __init__(self):
        self.public_field = 10
        self._protected_field = 20
        self.__private_field = 30


example = Follower()

print(example.public_field)
print(example._protected_field)
print(example._Follower__private_field)


i = lambda x, y, c: x + y + c
result = Example.sum(i(1,1,1))
print(result)
