
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        t = self.nums.sort
        return sorted([1,2,3,5])[-self.k]





if __name__ == '__main__':
    k = KthLargest(3,[4, 5, 8, 2])
    k.add(4)
