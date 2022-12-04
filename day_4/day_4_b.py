"""
ALGORITHM:
1. to find if one section partly overlaps the other, either one part of the section has to be equal or bigger than the other
2. compare the start and end of the sections to determine the result

The code is similar to part 1, and the only change is in the functions

def is_section_1_in_section_2(start_1, end_1, start_2, end_2):
def is_section_2_in_section_1(start_1, end_1, start_2, end_2):

we check for both start and end to be TRUE, instead we pass TRUE when at least one of them is true.

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


def is_section_1_partly_in_section_2(start_1, end_1, start_2, end_2):
    # where group 1 contains only one assignment
    if start_1 == end_1:
        if start_1 in range(start_2, (end_2 + 1)):
            return True
    elif start_1 in range(start_2, (end_2 + 1)) or end_1 in range(start_2, (end_2 + 1)):
        return True
    else:
        return False


def is_section_2_partly_in_section_1(start_1, end_1, start_2, end_2):
    # where group 2 contains only one assignment
    if start_2 == end_2:
        if start_2 in range(start_1, (end_1 + 1)):
            return True
    elif start_2 in range(start_1, (end_1 + 1)) or end_2 in range(start_1, (end_1 + 1)):
        return True
    else:
        return False


def find_overlapped_assignment_pairs():
    overlapped_assignment_pairs = 0
    with open("4_input.txt") as input_file:
        for line in input_file:
            group_1_start, group_1_end, group_2_start, group_2_end = find_sections_assigned_to_elf_group(line)
            if is_section_1_partly_in_section_2(group_1_start, group_1_end, group_2_start, group_2_end):
                overlapped_assignment_pairs += 1
            elif is_section_2_partly_in_section_1(group_1_start, group_1_end, group_2_start, group_2_end):
                overlapped_assignment_pairs += 1
    return overlapped_assignment_pairs


number_of_overlapped_assignment_pairs = find_overlapped_assignment_pairs()
print(number_of_overlapped_assignment_pairs)
