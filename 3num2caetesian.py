'''create a data type that takes 3 numbers
and stores the cartesian product as tuples'''
'''should be iterable in ascending numerical
order of the first tuple index'''
'''able to handle appropriate errors'''
import numbers

class Cartesian():
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self._validate()
        self.temp = [a,b,c]

    def _validate(self):
        error_type = 'start and stop parameter must be ineger'
        if not (isinstance(self.a, numbers.Number) and isinstance(self.b, numbers.Number) and isinstance(self.c, numbers.Number)):
            raise TypeError(error_type)

    def __iter__(self):
        print(self)
        return self

    # def __next__(self):
    #     print('**next state**')
    #     if self.current > self.stop:
    #         print('**********StopIteration***********', '\n', '******Enter next state******', '\n', '\n')
    #         raise StopIteration
    #     else:
    #         next_value = self.current
    #         print('Before current increment')
    #         print('next_value = ', next_value, ' self.current = ', self.current)
    #         self.current += 10
    #         print('After current increment')
    #         print('next_value = ', next_value, ' self.current = ', self.current)
    #         return next_value


if __name__ == '__main__':
    carte = Cartesian(1,3,2)
    # for value in carte:
    #     print(value,'\n')
    # by_ten = ByTen()
    # print('1')
    # for value in by_ten:
    #     print('2')
    #     print('current by_ten value:', value, '\n', '\n')


