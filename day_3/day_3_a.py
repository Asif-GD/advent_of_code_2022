"""
ALGORITHM:
1. Split the line into two parts (representing two rucksacks) and compare the elements to find duplicates.
2. Look up the priority_table to determine the priority of that element
3. Assign and add up the priority of all the duplicates as we find them, to a variable 'total_item_priority'

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


def get_two_rucksacks(line_from_input_file):
    line_length = len(line_from_input_file)

    # length is counted from 1, but string index starts at 0
    half_length = int(line_length / 2)
    # note -> explicit type conversion is required,
    # a division operation always results in a float even if it's a perfect division. for example 18/2 = 9.0
    # the end index is exclusive
    sack_1 = line_from_input_file[0:half_length]
    sack_2 = line_from_input_file[half_length:line_length]

    return sack_1, sack_2


"""
test -> def get_two_rucksacks(line_from_input_file):

input = "BWQhQzQwmhwWHbWCSRMRgjpjVDDRgDgVffgV"
print(input)
print(len(input))
rucksack_1, rucksack_2 = get_two_rucksacks(input)
print(rucksack_1, rucksack_2)
print(len(rucksack_1), len(rucksack_2))

"""


# it is unclear if there is exactly only one duplicate item between the rucksacks.
# else, I would simply break the for loop as soon as I find the duplicate and return it instead.
def find_duplicate_items_between_rucksacks(sack_1, sack_2):
    duplicates = ""
    for item in sack_1:
        duplicate = sack_2.find(item)
        # find() returns -1 if not found
        if duplicate != -1:
            duplicates += item
            # to prevent miscalculation from multiple copies of one element in sack_1 corresponding to one duplicate in sack_2
            # for example - sack_1 = "abciidZXpYF" sack_2 = "PLKJiDcEcNR"
            # in this case, two 'i' will account to two duplicates in sack_2, when in reality it should be counted as 1
            sack_2 = sack_2.replace(item, "")
    return duplicates


"""
test -> def find_duplicate_items_between_rucksacks(sack_1, sack_2):

duplicate_item = find_duplicate_items_between_rucksacks(rucksack_1, rucksack_2)
print(duplicate_item)

"""


def find_item_priority(duplicate_items):
    priority = 0
    for item in duplicate_items:
        priority += priority_table[item]
    return priority


"""
test -> def find_item_priority(duplicate_items):

item_priority = find_item_priority(duplicate_item)
print(item_priority)

"""


def calculate_total_item_priority():
    total_priority = 0
    with open("3_input.txt") as input_file:
        for line in input_file:
            rucksack_1, rucksack_2 = get_two_rucksacks(line)
            duplicate_item_list = find_duplicate_items_between_rucksacks(rucksack_1, rucksack_2)
            total_priority += find_item_priority(duplicate_item_list)
    return total_priority


print(calculate_total_item_priority())

"""
test -> def get_two_rucksacks(line_from_input_file):
test -> def find_duplicate_items_between_rucksacks(sack_1, sack_2):
test -> def find_item_priority(duplicate_items):

input = "BWQhQzQwmhwWHbWCSRMRgjpjVDDRgDgVffgV"
print(input)
print(len(input))
rucksack_1, rucksack_2 = get_two_rucksacks(input)
print(len(rucksack_1), len(rucksack_2))
print(rucksack_1, rucksack_2)

duplicate_item = find_duplicate_items_between_rucksacks(rucksack_1, rucksack_2)
print(duplicate_item)

item_priority = find_item_priority(duplicate_item)
print(item_priority)
"""
