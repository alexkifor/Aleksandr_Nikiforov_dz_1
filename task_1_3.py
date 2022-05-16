for number in range(1, 101):
    num_1 = number % 10
    num_2 = number // 10 % 10
    if num_1 == 1 and num_2 != 1:
        print(number, "процент")
    elif 5 > num_1 >= 2 and num_2 != 1:
        print(number, "процента")
    else:
        print(number, "процентов")
