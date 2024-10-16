numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
summary = 0
for i in numbers:
    if i is None:
        none_index = numbers.index(i)
    else:
        summary += i
arithmetic_mean = summary/len(numbers)
numbers[none_index] = arithmetic_mean


print("Измененный список:", numbers)
