import itertools
from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for type in list(J):
            for stone in list(S):
                if type == stone:
                    counter += 1

        return counter

    def anagramMappings(self, A, B):
        P = []
        for element in A:
            P.append(B.index(element))
        return P

    def num_uniq_emails(self, emails):
        uniq_emails = []
        for email in emails:
            uniq_name = email.split("@")[0].split("+")[0].replace(".", "")
            fixed_email = uniq_name + "@" + email.split("@")[1]
            if fixed_email not in uniq_emails:
                uniq_emails.append(fixed_email)
        return len(uniq_emails)

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dict = self.create_morse_dict()
        morse_words = []
        for word in words:
            morse_word = []
            for letter in list(word):
                morse_word.append(morse_dict.get(letter))
            morse_words.append(''.join(morse_word))
        return morse_words

    def create_morse_dict(self):
        morse_dict = {}
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                      "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        for letter, morse in zip(alphabet, morse_code):
            morse_dict[letter] = morse
        return morse_dict

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        string_S_without_backspaces = self.trigger_all_backspaces(S)
        string_T_without_backspaces = self.trigger_all_backspaces(T)
        return string_S_without_backspaces == string_T_without_backspaces

    def trigger_all_backspaces(self, data):
        if "#" in data:
            index = data.index("#")
            if index == 0:
                new_word = data[index + 1:]
                return self.trigger_all_backspaces(new_word)
            new_word = data[:index - 1] + data[index + 1:]
            return self.trigger_all_backspaces(new_word)
        else:
            return data

    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        squares_list = []
        for integer in A:
            squares_list.append(integer * integer)
        squares_list.sort()
        return squares_list

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        reversed_list = []
        for item in A:
            reversed_list.append(list(reversed(item)))

        inverted_list = []
        for i in reversed_list:
            inverted_item = []
            for a in i:
                if a == 0:
                    inverted_item.append(1)
                else:
                    inverted_item.append(0)
            inverted_list.append(inverted_item)
        return inverted_list

    def test_flipAndInvertImage(self):
        return self.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    def peakIndexInMountainArray(self, A):
        for i in xrange(len(A)):
            if A[i] > A[i + 1]:
                return i

    def test_peakIndexInMountainArray(self):
        return self.peakIndexInMountainArray([0, 1, 2])


    def isToeplitzMatrix_1(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        starting_pos = [0, 0]
        for move in list(moves):
            if move == "U":
                starting_pos[0] = starting_pos[0] + 1
            if move == "D":
                starting_pos[0] = starting_pos[0] - 1
            if move == "L":
                starting_pos[1] = starting_pos[1] + 1
            if move == "R":
                starting_pos[1] = starting_pos[1] - 1

        return starting_pos == [0, 0]

    def islandPerimeter(self, m):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        y = len(m)
        x = len(m[0])

        def abs(i, j):
            u = 1 if i > 0 and m[i - 1][j] == 1 else 0
            d = 1 if i < y - 1 and m[i + 1][j] == 1 else 0
            l = 1 if j > 0 and m[i][j - 1] == 1 else 0
            r = 1 if j < x - 1 and m[i][j + 1] == 1 else 0
            return 4 - u - d - l - r

        for i in range(y):
            for j in range(x):
                if m[i][j] == 1:
                    perimeter += abs(i, j)
        return perimeter

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return (set(list(xrange(1, len(nums) + 1))).difference(nums))

    def findDisappearedNumbers_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in xrange(len(nums)):
            index = nums[i] - 1
            index_2 = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        index = 0
        # find the index
        for ch in s:
            if count[ch] == 1:
                return index
            index += 1
        return -1

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = 2;
        for x in range(n + 1):
            if n == 0 and n == 1:
                return True
            while number <= n:
                number *= 2
            if number == n:
                return True
        return False

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        if n == 1: return True
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True

    def largestPrimeFactor(self, n):
        a = n
        b = 2
        c = 0
        while a != 1:
            if a % b == 0:
                if b > c:
                    c = b
                a = a / b
                b = 2
            b += 1
        return a

    def multiply_3_num(self):
        max = 0
        for x in reversed(xrange(999)):
            if x < 100:
                break
            for z in reversed(xrange(999)):
                if z < 100:
                    break
                mult = z * x
                if self.isPalindrome(mult):
                    if mult > max:
                        max = mult
                        list(z, x)
        return max

    def isPalindrome(self, l):
        list_s = list(str(l))
        return list_s == list(reversed(list_s))

    def test(self, max):
        for d in (i ** 2 for i in max):
            print(i)

    def PowTwoGen(self, max=0):
        n = 0
        while n < max:
            yield 2 ** n
            n += 1

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = "aieouAIEOU"
        char_s, char_e = 0, len(s) - 1
        while char_s < char_e:
            if s[char_s] in vowels and s[char_e] in vowels:
                s[char_s], s[char_e] = s[char_e], s[char_s]
                char_s += 1
                char_e -= 1
            if s[char_s] not in vowels: char_s += 1
            if s[char_e] not in vowels: char_e -= 1
        return "".join(s)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        for i in xrange(len(r) // 2):
            r[i], r[~i] = r[~i], r[i]
        return "".join(r)

    def pare(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if s == s[::-1] else False

    def canPermutePalindrome(self, s):
        dic = {}
        for item in s:
            dic[item] = dic.get(item,0) + 1
        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        for val in dic.values():
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True


    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [n for n,c in collections.Counter(nums).items() if c==1][0]


    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        for number in xrange(1,n+1):
            if number % 5 == 0 and number % 3 == 0:
                output.append("FizzBuzz")
                continue
            if number % 3 == 0:
                output.append("Fizz")
                continue
            if number % 5 == 0:
                output.append("Buzz")
                continue
            output.append(str(number))
        return output

    def nextGreaterElement(self, nums1, nums2):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []

        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))

        return ans

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        counter = 0
        if all(c in ('2', '5', '6', '9') for c in str(N)):
            counter = +1

        return counter


    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = 0
        num_dict = collections.Counter(nums)
        key = 0
        for i in nums:
            if num_dict[i] > maj:
                key = i
                maj = num_dict[i]

        return key

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-","").upper()[::-1]
        return "@".join(S[i:K+i] for i in xrange(0,len(S),K))[::-1]

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = ''
        for i in bin(num)[2:]:
            if i == '0':
                output += '1'
            else:
                output += '0'

        return int(output, 2)

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_list = [i for i in xrange(len(nums)+1)]

        return set(new_list).difference(nums)

        # dictionary

    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i

    def generate(self, num_rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        array = [[1] * (i + 1) for i in xrange(num_rows)]
        for i in xrange(num_rows):
            for j in xrange(1, i):
                array[i][j] = array[i - 1][j - 1] + array[i - 1][j]

        return array

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = reduce(lambda x, y: x + y, [int(i) for i in str(n)])
        if len([i for i in str(n)]) <= 1:
            return False
        if  number == 1:
            return True
        else:
            return self.isHappy(reduce(lambda x, y: (x ** 2) + (y ** 2), [int(i) for i in str(n)]))



    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict_n = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        number = 0
        number2 = 0
        for char in num1:
            number = 10 * number + dict_n[char]
        for char in num2:
            number2 = 10 * number2 + dict_n[char]
        return number1 + number2


    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return str(x) == reverse_slicing(str(x))


    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = Counter(str(bin(n)))
        return cnt['1']

if __name__ == '__main__':
    solution = Solution()
    solution.hammingWeight(00000000000000000000000000001011)
