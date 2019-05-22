class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.l = self.l + [x]

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.l.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.l) == 0

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.peek()
    param_3 = obj.pop()
    param_4 = obj.empty()