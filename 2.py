class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.integer_list = []

    def next(self, val):
        if len(self.integer_list) >= self.size:
            self.integer_list.pop(0)
        self.integer_list.append(val)
        return sum(self.integer_list)/(len(self.integer_list)*1.0)


class Solution(object):
    def twoSum(self, nums, target):
        for index, v in enumerate(nums):
            for i, v2 in enumerate(nums[1:]):
                if index == i:
                    continue
                if v + v2 == target:
                    return [index, i]


    def repeatedStringMatch(self, A, B):
        times = -(-len(B) // len(A)) # Equal to ceil(len(b) / len(a))
        for i in range(2):
          if B in (A * (times + i)):
            return times + i
        return -1


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.dict:
            prev_timestamp = self.dict[message]
            if timestamp - prev_timestamp >= 10:
                self.dict[message] = timestamp
                return True
            else:
                return False
        else:
            self.dict[message] = timestamp
            return True




if __name__ == "__main__":
     log = Logger()
#     log.shouldPrintMessage(1,"lol")
#     log.shouldPrintMessage(3,"lol")
#     log.shouldPrintMessage(11,"lol")
#    ob = MovingAverage(1)
#    ob = Solution()
#    ob.repeatedStringMatch("abcd","cdabcdab")
#    ob.twoSum([2,7,11,15],9)