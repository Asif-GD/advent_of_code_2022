"""
ALGORITHM:
1. to find if one section completely overlaps the other, the section has to be equal or bigger than the other
2. compare the start and end of the sections to determine the result

"""


def find_sections_assigned_to_elf_group(line_from_input_file):
    section_number = ""
    section_number_list = []
    for char in line_from_input_file:
        if char != '-' and char != ',':
            section_number += char
        else:
            section_number_list.append(section_number)
            section_number = ""
    section_number_list.append(section_number)

    group_1_section_start = int(section_number_list[0])
    group_1_section_end = int(section_number_list[1])
    group_2_section_start = int(section_number_list[2])
    group_2_section_end = int(section_number_list[3])

    return group_1_section_start, group_1_section_end, group_2_section_start, group_2_section_end


"""
test -> find_sections_assigned_to_elf_group(line_from_input_file):

group_1_start, group_1_end, group_2_start, group_2_end = find_sections_assigned_to_elf_group("12-80,12-81")
print(group_1_start, group_1_end, group_2_start, group_2_end)
"""


def is_section_1_in_section_2(start_1, end_1, start_2, end_2):
    # where group 1 contains only one assignment
    if start_1 == end_1:
        if start_1 in range(start_2, (end_2 + 1)):
            return True
    elif start_1 in range(start_2, (end_2 + 1)) and end_1 in range(start_2, (end_2 + 1)):
        return True
    else:
        return False


"""
test -> is_section_1_in_section_2(start_1, end_1, start_2, end_2):
print(is_section_1_in_section_2(5, 7, 7, 9))
"""


def is_section_2_in_section_1(start_1, end_1, start_2, end_2):
    # where group 2 contains only one assignment
    if start_2 == end_2:
        if start_2 in range(start_1, (end_1 + 1)):
            return True
    elif start_2 in range(start_1, (end_1 + 1)) and end_2 in range(start_1, (end_1 + 1)):
        return True
    else:
        return False


def find_overlapped_assignment_pairs():
    overlapped_assignment_pairs = 0
    with open("4_input.txt") as input_file:
        for line in input_file:
            group_1_start, group_1_end, group_2_start, group_2_end = find_sections_assigned_to_elf_group(line)
            if is_section_1_in_section_2(group_1_start, group_1_end, group_2_start, group_2_end):
                overlapped_assignment_pairs += 1
            elif is_section_2_in_section_1(group_1_start, group_1_end, group_2_start, group_2_end):
                overlapped_assignment_pairs += 1
    return overlapped_assignment_pairs


print(find_overlapped_assignment_pairs())
