def read_input():
    with open('input.inp', 'r') as file:
        list_one = []
        list_two = []
        for line in file:
            element_one = int(line.split("  ")[0])
            element_two = int(line.split("  ")[1].split("\n")[0])
            list_one.append(element_one)
            list_two.append(element_two)
    
    sorted_one = sorted(list_one)
    sorted_two = sorted(list_two)

    return sorted_one, sorted_two

def part_one():
    list_one, list_two = read_input()
    distance = 0

    for i, j in zip(list_one, list_two):
        distance += abs(i-j)

    return distance


def find_number_in_list(number, second_list):
    occurrences = 0
    for i in second_list:
        if (number == i):
            occurrences += 1

    return occurrences


def part_two():
    list_one, list_two = read_input()

    similarity_idx = 0
    for i in list_one:
        similarity_idx += i * find_number_in_list(i, list_two)

    return similarity_idx

print("Result part one", part_one())
print("Result part two", part_two())