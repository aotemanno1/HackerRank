'''Demonstrate iteration using __getitem__'''

from random import randint

class LuckyBall():
    '''an iterable with six random numbers'''
    def __init__(self):
        print('\n','###initial state###')
        '''Generate a list of six unique random integers'''
        self.nums = []
        while len(self.nums) < 6:
            print('check the loop-------')
            rand_num = randint(1, 20)
            if not rand_num in self.nums:
                print('append it!')
                self.nums.append(rand_num)

    def __getitem__(self, index):
        print('\n','###getitem state####')
        return self.nums[index]

    def __len__(self):
        print('\n','###length state###')
        return len(self.nums)

if __name__ == '__main__':
    print('\n','###main###')
    lotto = LuckyBall()
    print('\n','###after construction###')
    for num in range(len(lotto)):
        print('The nubmer with index %s is %i' %(num,lotto[num]))

    print ('The last number was %i' % lotto[-1])
    print ('The first number was %i' % lotto[0])
    print ('The second number was %i' % lotto.__getitem__(1))

for num in lotto:
    print(num)






