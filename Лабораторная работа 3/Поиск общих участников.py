# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, sep = ","):
    total_set = set(participants_first_group.split(sep)).intersection(set(participants_second_group.split(sep)))
    total_list = sorted(total_set)
    return total_list
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))