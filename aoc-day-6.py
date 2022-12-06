
def find_first_marker(data, distinct_chars):
    for i in range(0, len(data) - distinct_chars):
        # 'set' turns a list or string into a set which, by 
        #  definition contains unique values.
        if len(set(data[i: i+distinct_chars])) == distinct_chars:
            found = i
            break
    return found + distinct_chars


with open('aoc-day-6.txt') as f:
    data = f.read()

print(f"first marker after character {find_first_marker(data, 4)}")

print(f"first marker after character {find_first_marker(data, 14)}")
