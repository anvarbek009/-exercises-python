# from datetime import datetime
# from time import perf_counter
# t1=perf_counter()
# list_of_numbers=list(range(1_000_000))
# result=[i**2 for i in list_of_numbers]
# t2=perf_counter()
# print(t2-t1)

# def filter_func(x):
#     return x % 2 != 0

# print(filter_func(32))
#
#
# def filter_func2(x):
#     return not x.isupper()


# def square_func(x):
#     return x**2


# def to_grade(x):
#     if x >= 90:
#         return "A"
#     elif 80 <= x < 90:
#         return "B"
#     elif 70 <= x < 80:
#         return "C"
#     elif 65 <= x < 70:
#         return "D"
#     return "F"


# def main():
#     nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
#     chars = "abcDeFGHiJklmnoP"
#     grades = (81, 89, 94, 78, 61, 66, 99, 74)

#     odds = list(filter(filter_func, nums))
#     print(odds)  # [1, 5, 13, 381, 47]

#     lowers = list(filter(filter_func2, chars))
#     print(lowers)  # ['a', 'b', 'c', 'e', 'i', 'k', 'l', 'm', 'n', 'o']

#     squares = list(map(square_func, nums))
#     print(squares)  # [1, 64, 16, 25, 169, 676, 145161, 168100, 3364, 2209]

#     grades_sorted = sorted(grades)
#     letters = list(map(to_grade, grades_sorted))
#     print(grades_sorted, letters)  # [61, 66, 74, 78, 81, 89, 94, 99] ['F', 'D', 'C', 'C', 'B', 'B', 'A', 'A']

#     zipped = zip(grades_sorted, letters)
#     print(list(zipped))  # [(61, 'F'), (66, 'D'), (74, 'C'), (78, 'C'), (81, 'B'), (89, 'B'), (94, 'A'), (99, 'A')]


# if __name__ == "__main__":
#     main()

# Homework
# 1
# my_dict={
#     'Anvar':33,
#     'Bekzod':27,
#     'Sardor':12,
#     'Zubayr':20
# }

# print(sorted(my_dict.items(), key=lambda x: x[1])) 

# 2
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# merged_dict = {}
# merged_dict.update(dic1)
# merged_dict.update(dic2)
# merged_dict.update(dic3)
# print(merged_dict)

# 3
# def superr(n):
#     all={}
#     for i in range(1,n+1):
#         one={i:i**2}
#         all.update(one)
#     print(all)
# superr(15)

# 4
# dic={
#     1:10, 2:20,
#     3:30, 4:40,
#     5:50, 6:60
# }

# print(sum(dic.values()))

# 5
# dic={
#     1:10, 2:20,
#     3:30, 4:40,
#     5:50, 6:60
# }
# print(max(dic.values()))

# 6
# dic={
#     1:10, 2:20,
#     3:30, 4:40,
#     5:50, 6:60
# }
# print(min(dic.values()))

# 7
# from collections import Counter

# def merge_dicts(d1, d2):
#     counter1 = Counter(d1)
#     counter2 = Counter(d2)
#     merged_counter = counter1 + counter2
#     return dict(merged_counter)

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
 
# print(merge_dicts(d1, d2))

# 8
    # def unique_values(lst):
    #     unique_set = set()
    #     for d in lst:
    #         for value in d.values():
    #             unique_set.add(value)
    #     return unique_set

    # lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    
    # print(unique_values(lst))
# 9
# def count_characters(word):
#     char_count = {}
#     for char in word:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     for char, count in char_count.items():
#         print(f"{char} {count} ta")

# word = input("So'zni kiriting: ")
# count_characters(word)

# 10
# def find_most_and_least_used_characters(word):
#     char_count = {}
#     for char in word:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     most_used = max(char_count, key=char_count.get)
#     least_used = min(char_count, key=char_count.get)
    
#     return most_used, least_used

# word = "mexanizasiyalashtirilganmi"
# most_used, least_used = find_most_and_least_used_characters(word)
# print(f"Eng ko'p ishlatilgan harf: {most_used}")
# print(f"Eng kam ishlatilgan harf: {least_used}")

# 11
# from cyrtranslit import to_latin

# def cyrillic_to_latin(word):
#     latin_word = to_latin(word)
#     return latin_word

# kirill_word = "крилл чада сўз"
# latin_word = cyrillic_to_latin(kirill_word)
# print(latin_word)

# 12
# from cyrtranslit import to_cyrillic

# def latin_to_cyrillic(word):
#     latin_word = to_cyrillic(word)
#     return latin_word

# kirill_word = "Lotin so'z"
# latin_word = latin_to_cyrillic(kirill_word)
# print(latin_word)
