# s = int(input('Son kiriting\n=>'))
# a=[]
# for i in range(0,s):
#     a.append(i)
#     b=a[i]+a[i]+1
# print(b)


# Homwwork
# 1
list1=[1, 1, 3, 4, 4, 5, 6, 7]
list2=[0, 1, 2, 3, 4, 4, 5, 7, 8]
for i in list2:
   list1.append(i)
print(sum(list1)/len(list1 ))

# 2   
a=[1, 4, 3, 9]
b="RM"
c=[]
for i in a:
   c.append(f'RM{i}')
print(c)

# 3
lists = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
max_sum_list = max(lists, key=sum)
print(max_sum_list)

# 4
input_list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
integer_count = sum(isinstance(x, int) for x in input_list)
print(integer_count)

# 5
input_list = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
max_count = max(set(input_list), key=input_list.count)
print(f"{max_count} -> {input_list.count(max_count)} marta")

# 6
def add_one(nums):
    num = int(''.join(map(str, nums))) + 1
    return [int(i) for i in str(num)]

input_list = [1,2,3]
output_list = add_one(input_list)
print(output_list)

# 7
def square_list():
    numbers = input().split()
    squares = [int(num)**2 for num in numbers]
    return squares

print(square_list())


# 8
def find_common_max(list1, list2):
    common_max = max(set(list1) & set(list2))
    return common_max

list1 = [1, 4, 3, 9]
list2 = [2, 6, 8, 9]
print(find_common_max(list1, list2))

# 8

def fibonacci(n):
    fib_sequence = [1, 2]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

n = int(input("Kiritilgan songacha eng yaqin bolgan Fibonachi sonlarini toping: "))
print(fibonacci(n))

# 10
nterms = int(input("Nechta son chiqsin?\n=>"))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Musbat son kiriting\n=>")
elif nterms == 1:
   print("Fibonacci sonlar dan katta",nterms,":")
   print(n1)
else:
   print("Fibonacci sonlar:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       