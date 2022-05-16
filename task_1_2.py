numbers = []
for number in range(1, 1000, 2):
    numbers.append(number ** 3)
# a.
numbers_1 = []
for number_1 in numbers:
    num_1_1 = number_1 % 10
    num_1_2 = number_1 // 10 % 10
    num_1_3 = number_1 // 100 % 10
    num_1_4 = number_1 // 1000 % 10
    num_1_5 = number_1 // 10000 % 10
    num_1_6 = number_1 // 100000 % 10
    num_1_7 = number_1 // 1000000 % 10
    num_1_8 = number_1 // 10000000 % 10
    num_1_9 = number_1 // 100000000
    total = num_1_1 + num_1_2 + num_1_3 + num_1_4 + num_1_5 + num_1_6 + num_1_7 + num_1_8 + num_1_9
    if total % 7 == 0:
        numbers_1.append(number_1)
print(sum(numbers_1))
# b.
numbers_2 = []
numbers_3 = []
for number_1 in numbers:
    number_2 = number_1 + 17
    numbers_2.append(number_2)
for number_2 in numbers_2:
    num_2_1 = number_2 % 10
    num_2_2 = number_2 // 10 % 10
    num_2_3 = number_2 // 100 % 10
    num_2_4 = number_2 // 1000 % 10
    num_2_5 = number_2 // 10000 % 10
    num_2_6 = number_2 // 100000 % 10
    num_2_7 = number_2 // 1000000 % 10
    num_2_8 = number_2 // 10000000 % 10
    num_2_9 = number_2 // 100000000
    total = num_2_1 + num_2_2 + num_2_3 + num_2_4 + num_2_5 + num_2_6 + num_2_7 + num_2_8 + num_2_9
    if total % 7 == 0:
        numbers_3.append(number_2)
print(sum(numbers_3))
# c.
numbers_4 = []
for number_3, number in enumerate(numbers):
    numbers[number_3] = number + 17
for number_3 in numbers:
    num_3_1 = number_3 % 10
    num_3_2 = number_3 // 10 % 10
    num_3_3 = number_3 // 100 % 10
    num_3_4 = number_3 // 1000 % 10
    num_3_5 = number_3 // 10000 % 10
    num_3_6 = number_3 // 100000 % 10
    num_3_7 = number_3 // 1000000 % 10
    num_3_8 = number_3 // 10000000 % 10
    num_3_9 = number_3 // 100000000
    total = num_3_1 + num_3_2 + num_3_3 + num_3_4 + num_3_5 + num_3_6 + num_3_7 + num_3_8 + num_3_9
    if total % 7 == 0:
        numbers_4.append(number_3)
print(sum(numbers_4))
