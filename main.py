# Fill in the functions content & think about the return values. (Don't forget to remove the 'pass' statement)
# In questions with classes you can create the class & write the logic inside the function.

# Class
from typing import List


def q1a(input_num):
    class PrimeSmallerThan:
        def __init__(self, n):  # add parameters
            self.cur = 2
            self.last = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.last <= self.cur:
                raise StopIteration()
            nextCur = self.cur + 1
            found = False
            while not found:
                for i in range(2, nextCur):
                    if nextCur % i == 0:
                        break
                else:
                    found = True
                nextCur = nextCur + 1

            difference = nextCur - self.cur - 1
            self.cur = nextCur - 1
            return self.cur - difference

    instance = PrimeSmallerThan(input_num)  # add parameters
    return instance


# Generator
def q1b(input_num):
    nextCur = 2
    last = input_num
    while nextCur < last:
        for i in range(2, nextCur):
            if nextCur % i == 0:
                break
        else:
            yield nextCur
        nextCur = nextCur + 1


# List comprehension
def q2(n):
    return [x for x in range(2, n) if n % x == 0]


# One line
# m - min, n - max
def q3(m, n):
    return ["prime" if num > 1 and len([i for i in range(2, num // 2 + 1) if num % i == 0]) == 0 else "not prime" for
            num
            in range(m, n + 1)]


# Generator
# m - min, n - max
def q4(m, n):
    for i in range(m, n):
        if i % 2 == 0 and i % 100 != 0 and ((i % 10) % (i // 10 % 10)) == 0:
            yield i


# One line
def q5(str):
    return {s: str.count(s) for s in str}


# Generator
def q6a(str1, str2):
    for char1, char2 in zip(str1, str2):
        if char1 == char2:
            yield char1


# Class
def q6b(str1, str2):
    class StringsCompare:  # add class functions
        def __init__(self, str1, str2):
            self.str1 = str1
            self.str2 = str2
            self.cur = 0
            self.last = min(len(str1), len(str2))

        def __iter__(self):
            return self

        def __next__(self):
            if self.cur >= self.last:
                raise StopIteration()
            for i in range(self.cur, self.last):
                if self.str1[i] == self.str2[i]:
                    self.cur = i + 1
                    return self.str1[i]
                self.cur = i





    instance = StringsCompare(str1, str2)  # add parameters
    return instance


# One line
def q7(char_list, index_list):
    #   return ''.join(char for char in )
    pass

# Generator
def q8a(a, b):
    maxNum = max(a,b)
    minNum = min(a,b)
    i = minNum
    while True:
        while i < maxNum:
            yield i
            i += 1
        while i > minNum:
            yield i
            i += -1



# q8b

def processor():
    while True:
        value = yield
        print(f'Processing {value}')



data_processor = processor()

print(type(data_processor))


# Remove the '#' to run the corresponding test
# Don't forget to fill in the parameters.
if __name__ == "__main__":
    # q1a #
    #  input_num = 100
    # for num in q1a(input_num):
    #     print(num)

    # q1b #
    #   for num in q1b(100):
    #  	print(num)

    # q2 #
    #  print(q2(24))

    # q3 #
    # print(q3(2, 14))

    # q4 #
    #  for c in q4(12, 45):
    #     print(c)

    #   q5 #
    #print(q5("this is a simple string"))

    # q6a #
    # for c in q6a("like", "love"):
    # 	print(c)

    # q6b #
    # for c in q6b("like", "love"):
    # 	print(c)

    # q7 #
    #print(q7(['a', 'h', 'f', 'e', 'y', 'u'], [1, 5, 3, 6, 2, 4]))

    # q8a #
    # for c in q8a(3, 11):
    #	print(c)

    # q8b #

    # instanc = processor()  
    # instanc.send(None)  
    #for x in range(1, 5):
    #   instanc.send(x)  


#q9c
    cars = [] #we could also add all at once but i wanted to make it simmiler to the screenshot of java code
    cars.append("Volvo")
    cars.append("BMW")
    cars.append("Ford")
    cars.append("Mazda")
    iterator = iter(cars)
    print(next(iterator))

    pass
