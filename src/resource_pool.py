import math


class ResourcePool:
    def __init__(self, amount, length):
        self.amount = amount
        self.pool = [amount] * length

    # Make a reservation for a certain amount of resources for a certain period in time
    def allocate(self, time, amount, length):
        self._amount_check(amount)
        for i in range(time, time + length):
            if self.pool[i] >= amount:
                self.pool[i] -= amount
            else:
                raise Exception('You can not allocate that amount of resources during that time. Time = ' + length +
                                ' Amount = ' + amount)

    # Find first moment starting from start where one can make a reservation for an amount of resources for a certain
    # period in time
    def get_earliest_time(self, start, amount, length):
        length = math.ceil(length)
        if length == 0:
            return start
        start = math.ceil(start)
        # print('got', start, amount, length)
        if amount > self.amount:
            return None

        start_time = None
        counter = 0
        # Find earliest moment for reservation
        for i in range(start, len(self.pool)):
            # print('\t', i, ':')
            if self.pool[i] >= amount:
                counter += 1
            else:
                counter = 0
            if counter == length:
                start_time = i - counter + 1
                break
        # Check if possible
        if start_time is None:
            self._double_pool()
            print('doubling...')
            return self.get_earliest_time(start, amount, length)
        else:
            return start_time

    # Double the pool in time
    def _double_pool(self):
        self.pool.extend([self.amount] * len(self.pool))
        if len(self.pool) > 100000:
            raise Exception('List too long. Something went wrong.')

    def _amount_check(self, amount):
        if amount > self.amount:
            raise Exception('You can not allocate that amount of resources. Amount = ' + amount)
