def read_input():
    lists = []
    with open('day2/input.inp', 'r') as file:
        for line in file:
            elements = line.split("\n")[0].split(" ")
            lists.append([int(item) for item in elements])
           
    return lists

def is_safe(list):
    safe = True
    prev_diff = 0
    for i in range(len(list)-1):
        diff = list[i] - list[i+1]
        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            return safe
        if prev_diff != 0:
            if (prev_diff > 0 and diff < 0):
                return False
            if (prev_diff < 0 and diff > 0):
                return False
        prev_diff = diff
    
    return safe

def part_one():
    inputs = read_input()

    safes = 0

    for i in inputs:
        if is_safe(i):
            safes +=1
    
    return safes

print(part_one())
