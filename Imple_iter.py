class ByTen():
    def __init__(self, start=0, stop=100):
        print('**initial state**')
        self.start = start
        self.stop = stop
        self._validate()
        self.current = start

    def _validate(self):
        print('**validate state**')
        error_type = 'start and stop parameter must be ineger'
        error_value = ' start >= stop, unable to iterate'
        if not(isinstance(self.start, int) and isinstance(self.stop, int)):
            raise TypeError(error_type)
        if self.start >= self.stop:
            raise ValueError(error_value)

    def __iter__(self):
        print('**iter state**')
        print(self)
        return self

    def __next__(self):
        print('**next state**')
        if self.current > self.stop:
            print('**********StopIteration***********', '\n', '******Enter next state******', '\n', '\n')
            raise StopIteration
        else:
            next_value = self.current
            print('Before current increment')
            print('next_value = ', next_value, ' self.current = ', self.current)
            self.current += 10
            print('After current increment')
            print('next_value = ', next_value, ' self.current = ', self.current)
            return next_value

if __name__ == '__main__':
    print('**main state**')
    by_ten = ByTen()
    print('1')
    for value in by_ten:
        print('2')
        print('current by_ten value:', value, '\n', '\n')


    print('****Print 1000 to 1030****')
    by_ten = ByTen(1000, 1030)
    for value in by_ten:
        print('current by_ten value', value)

    try:
        by_ten = ByTen(10, 10)
    except ValueError as err:
        print('Handled ValueError:', err)

    try:
        by_ten = ByTen('a', 'z')
    except TypeError as err:
        print('Handled TypeError:', err)

