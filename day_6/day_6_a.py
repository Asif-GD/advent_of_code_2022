"""
ALGORITHM:
1. four continuous 'char' from the string would be added to a python set()
2. Python set() doesn't allow duplicates
3. if len(set()) is 4, that substring is the unique 'start-of-packet marker'

"""


def get_line_from_input_file():
    with open("6_input.txt") as input_file:
        line_from_input_file = input_file.readline()
    return line_from_input_file


"""
test -> get_line_from_input_file():
print(get_line_from_input_file())
"""


def find_start_of_packet_marker():
    start_of_packet_marker = set()
    line_from_input_file = get_line_from_input_file()
    start_index = 0
    end_index = 4
    nth_iteration = 0
    while True:
        for char_position in range(start_index, end_index):
            start_of_packet_marker.add(line_from_input_file[char_position])
        if len(start_of_packet_marker) < 4:
            start_of_packet_marker = set()
            start_index += 1
            end_index += 1
            nth_iteration += 1
        else:
            return nth_iteration + 4


print(find_start_of_packet_marker())
