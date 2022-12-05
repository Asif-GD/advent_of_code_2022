"""
ALGORITHM:
1. Every three lines of the file is added to a list 'group'
2. Three 'rucksacks' are obtained from each 'group'
3. Each element in rucksack_1 is compared with both rucksack_2 & rucksack_3 AND there can be only one across all three.
4. Look up the priority_table to determine the priority of that element
5. Assign and add up the priority of all the 'badge_item' as we find them, to a variable 'total_badge_item_priority'

"""

# fun fact: I built the priority table using this ;)
# def build_priority_table():
#     count = 1
#     for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         print(f"\'{char}\': {count},")
#         count += 1


priority_table = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,
    'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
    'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
}


def get_rucksacks_from_elf_group(three_lines_list):
    sack_1 = three_lines_list[0]
    sack_2 = three_lines_list[1]
    sack_3 = three_lines_list[2]

    return sack_1, sack_2, sack_3


# there is only item that is duplicate across all the three elves' rucksacks
def find_badge_item_in_group(sack_1, sack_2, sack_3):
    duplicate_item = ""
    for item in sack_1:
        duplicate_item_1_2 = sack_2.find(item)
        duplicate_item_1_3 = sack_3.find(item)
        if duplicate_item_1_2 != -1 and duplicate_item_1_3 != -1:
            duplicate_item = item
            break

    return duplicate_item


def find_item_priority(duplicate_items):
    priority = 0
    for item in duplicate_items:
        priority += priority_table[item]
    return priority


def calculate_total_item_priority():
    with open("3_input.txt") as input_file:
        group = []
        line_count = 0
        total_priority = 0
        for line in input_file:
            group.append(line)
            line_count += 1
            if line_count == 3:
                rucksack_1, rucksack_2, rucksack_3 = get_rucksacks_from_elf_group(group)
                badge_item_of_group = find_badge_item_in_group(rucksack_1, rucksack_2, rucksack_3)
                total_priority += find_item_priority(badge_item_of_group)
                group = []
                line_count = 0

    return total_priority


print(calculate_total_item_priority())
