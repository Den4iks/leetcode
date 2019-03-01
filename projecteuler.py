import itertools
import unittest
import math
class ProjectEulerSolutions:

    def sumOfMutliplies(self, param):
        sum = 0
        for x in range(param):
            if (x % 3 == 0) or (x % 5 == 0):
                sum += x
        return sum

    def sumOfFibonacci(self, param):
        sum = 0
        a = 1
        b = 2
        c = a + b
        while c <= param:
            a = b
            b = c
            c = a + b
            if (c % 2 == 0):
                sum += c
        return sum

    def smallestNumber(self):
        for i in xrange(200000000, 1000000000):
            if all(i%j==0 for j in xrange(1,20)):
                return i

    def smallestNumberTrick(self):
        from fractions import gcd
        from functools import reduce
        def lcm(a, b):
            "Calculate the lowest common multiple of two integers a and b"
            return a * b // gcd(a, b)

        reduce(lcm, xrange(1, 10 + 1))

    def sumSquareDiffernce(self,n):
         sum_sq = sum([i**2 for i in xrange(1,n+1)])
         sq_sum = (sum(xrange(1,n+1)))**2
         result = sq_sum - sum_sq

    def getPrime(self,n):

        attemp = 3
        list_of_pn = [2]
        while len(list_of_pn) < n:
            if all(attemp % i !=0 for i in list_of_pn):
                list_of_pn.append(attemp)
            attemp+=2
        return list_of_pn[-1]

    def find_adjacent_digit(self, n_number,ad_dig):
        greatest_product = 0
        start = 0
        end = n_number
        stop = True
        string_l = len(ad_dig)
        while stop:
            value=ad_dig[start:end]
            mult = reduce(lambda x,y: x*y, (int(i) for i in list(value)))
            if greatest_product < mult: greatest_product=mult
            if string_l < end+1:
                stop = False
            start +=1
            end +=1
        return greatest_product

    def pythagorean_triplet(self, n):
        for b in xrange(1,n):
            for a in xrange(1,b):
                c = math.sqrt(a*a+b*b)
                if c%1==0:
                    print(reduce(lambda x,y: x*y, ([a,b,c])))




    def sum_prime(self, n):
        attemp = 3
        prime_list = [2,3]
        while attemp<n:
            if all(attemp%j!=0 for j in prime_list):
                prime_list.append(attemp)
            attemp+=2
        print(sum(x for x in prime_list))

    def triangle_number(self,number):
        triangle_number = 0
        for i in itertools.count(start=0, step=1):
            triangle_number +=i
            if len([i for i in xrange(1,triangle_number+1) if triangle_number%i==0]) >=number:
                print(triangle_number)
                return triangle_number

if __name__ == "__main__":
    solution = ProjectEulerSolutions()
    solution.triangle_number(300)