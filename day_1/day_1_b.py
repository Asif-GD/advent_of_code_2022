"""
ALGORITHM:
1. lines from the input file is read, added with the value of the previous line
and stored to a variable - 'total_calories_of_current_elf'
2. when a line break is encountered in the input file, the current value of the variable 'total_calories_of_current_elf'
is compared with another variable - 'highest_calorie_count'
3. if highest_calorie_count < total_calories_of_current_elf:
    highest_calorie_count = total_calories_of_current_elf
4. total_calories_of_current_elf is reinitialized to 0 at every encounter of an empty line in the input file.
4. this continues until the end of the input file.

"""


def most_calories_by_an_elf():
    total_calories_of_current_elf = 0
    highest_calorie_count = 0

    with open("1_input.txt") as input_file:
        calories_list = []
        for line in input_file:
            if line.isspace():
                # an empty line in the input file indicates the end of the current elf's inventory.
                calories_list.append(total_calories_of_current_elf)
                total_calories_of_current_elf = 0
            else:
                total_calories_of_current_elf += int(line)

    calories_list.sort(reverse=True)
    highest_calorie_count = calories_list[0] + calories_list[1] + calories_list[2]
    print(highest_calorie_count)


most_calories_by_an_elf()
