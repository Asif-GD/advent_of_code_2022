"""
Initial Stack of crates
[Q]         [N]             [N]
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]
 1   2   3   4   5   6   7   8   9

"""

# stack_of_crates = {
#     '1': ['Z', 'N'],
#     '2': ['M', 'C', 'D'],
#     '3': ['P'],
# }

stack_of_crates = {
    '1': ['B', 'V', 'S', 'N', 'T', 'C', 'H', 'Q', ],
    '2': ['W', 'D', 'B', 'G', ],
    '3': ['F', 'W', 'R', 'T', 'S', 'Q', 'B', ],
    '4': ['L', 'G', 'W', 'S', 'Z', 'J', 'D', 'N', ],
    '5': ['M', 'P', 'D', 'V', 'F', ],
    '6': ['F', 'W', 'J', ],
    '7': ['L', 'N', 'Q', 'B', 'J', 'V', ],
    '8': ['G', 'T', 'R', 'C', 'J', 'Q', 'S', 'N', ],
    '9': ['J', 'S', 'Q', 'C', 'W', 'D', 'M', ],
}


def decipher_crane_instructions(line_from_input_file):
    line_after_split = line_from_input_file.split(" ")
    number_of_crates = int(line_after_split[1])
    from_stack = line_after_split[3]
    # while reading lines from a file, the last char is '\n'
    # for example "move 1 from 2 to 1", the last char in "1\n"
    to_stack = line_after_split[5][0]

    return number_of_crates, from_stack, to_stack


"""
test -> decipher_crate_instructions(line_from_input_file):

number_of_crates, from_stack, to_stack = decipher_crane_instructions("move 1 from 1 to 2")
print(number_of_crates, from_stack, to_stack)
"""


def execute_crane_instructions(number_of_crates, from_stack, to_stack):
    crate_stack = []
    total_crates_from_stack = len(stack_of_crates[from_stack])

    for crate_position in reversed(range(total_crates_from_stack)):
        crate_to_move = stack_of_crates[from_stack].pop(crate_position)
        crate_stack.append(crate_to_move)
        number_of_crates -= 1
        if number_of_crates == 0:
            crate_stack.reverse()
            stack_of_crates[to_stack].extend(crate_stack)
            break


"""
test -> execute_crane_instructions(number_of_crates, from_stack, to_stack):
execute_crane_instructions(3, "6", "2")
"""


def top_crate_at_all_stacks():
    # executes all crane instructions
    with open("5_input.txt") as input_file:
        for line in input_file:
            number_of_crates, from_stack, to_stack = decipher_crane_instructions(line)
            execute_crane_instructions(number_of_crates, from_stack, to_stack)

    # get top crates from all the stacks
    top_crates = ""
    for stack_number in stack_of_crates:
        total_crates_in_stack = len(stack_of_crates[stack_number])
        if total_crates_in_stack == 0:
            top_crates += stack_of_crates[stack_number]
        else:
            last_crate_position = total_crates_in_stack - 1
            top_crates += stack_of_crates[stack_number][last_crate_position]

    return top_crates


print(top_crate_at_all_stacks())
