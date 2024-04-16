# a=('John','Charles','Mike')
# b=('Jenny','Christy','Monica','Jonny')
# result=list(zip(a,b))
# def generate_list(obj):
#     for i in obj:
#         yield i

# h=generate_list(result)
# print(next(h))
# print(next(h))
# print(next(h))



# def fibonacci(n):
#     fib_sequence = [1, 2]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence[:n]

# n = int(input("Kiritilgan songacha eng yaqin bolgan Fibonachi sonlar topish uchun son kiriting: "))
# print(fibonacci(n))


# def fibn(n):
#     fibn_num = [0, 1]
#     if n in fibn_num:
#         return fibn_num[n]
#     else:
#         [fibn_num.append(fibn_num[-1] + fibn_num[-2]) for i in range(2, n+1)]
#         return fibn_num[n]
# print(fibn(5))
# print(fibn(3))
# print(fibn(19))


# Homework
# 1
from datetime import datetime

from datetime import datetime

def seconds_between_clocks(time1, time2):
    t1 = datetime.strptime(time1, "%H:%M:%S")
    t2 = datetime.strptime(time2, "%H:%M:%S")
    
    diff = abs((t2 - t1).total_seconds())
    return int(diff)

time1 = "10:15:30"
time2 = "11:20:45"
print(seconds_between_clocks(time1, time2))

time1 = "23:59:59"
time2 = "00:00:01"
print(seconds_between_clocks(time1, time2))  

# 2

def even_divisors(n):
    for i in range(2, n):
        if n % i == 0 and i % 2 == 0:
            yield i

son=int(input('Necha songacha bolsin\n=>'))
print(f"Juft bo'luvchilar: {list(even_divisors(son))}") 

# 3

def prime_generator(n):
    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num

n = 20
print(f"Tub sonlar: {[prime for prime in prime_generator(n)]}") 

# 4
def prime_factors_generator(n):
    while n % 2 == 0:
        yield 2
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            yield i
            n = n // i

    if n > 2:
        yield n

num = 315
print(f"{num} ning tub bo'luvchilari: {[prime for prime in prime_factors_generator(num)]}") 

# 5 

def even(b):
    o=[]
    for i in b:
        if  i%2==0:
            o.append(i)
    yield o

u=even([13,16,20,27,31])
print(next(u))

# 6

def sentences(b):
    o={}
    for i in b:
        o[i]=f'{len(i)} ta harf'
    yield o

y=sentences(['Avaz','Bekzod','Qobil'])
print(next(y))

# 7
def sentence(b):
    o={}
    for i in b:
        if len(i)>5:
            o[i]=f'{len(i)} ta harf'
    yield o

w=sentence(['Avaz','Bekzod','Qobil'])
print(next(w))

# 8

def three_times_occurrences(lst):
    seen = {}
    for num in lst:
        seen[num] = seen.get(num, 0) + 1
        if seen[num] == 3:
            yield num

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6]
print(list(three_times_occurrences(numbers)))