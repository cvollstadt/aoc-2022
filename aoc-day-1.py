
with open('aoc-day-1.txt') as f:
    data = f.read()

# list of lists
elves = [elf.split('\n')  for elf in data.split('\n\n')]

# convert to int 
elves_int = [[int(cal) for cal in elf if len(cal) > 0] for elf in elves]

# sum each elf
elves_sum = [sum(elf) for elf in elves_int]

elves_sum.sort(reverse=True)

top_elf = elves_sum[0]

print(top_elf)

top_three = sum(elves_sum[:3])

print(top_three)

