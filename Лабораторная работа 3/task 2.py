# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, delimeter=","):
    delimeter = input("Введите разделитель")
    return set(str1.split(f"{delimeter}")).intersection(str2.split(f"{delimeter}"))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
