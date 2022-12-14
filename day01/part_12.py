cals = 0
elves = []

for line in open('day01/1.in').read().splitlines():
    if line:
        cals += int(line)
    else:
        elves.append(cals)
        cals = 0

elves.append(cals)  # Don't forget the last one
elves.sort(reverse=True)

part_1 = elves[0]
part_2 = sum(elves[:3])

print(f'{part_1 = }')
print(f'{part_2 = }')

assert part_1 == 69626
assert part_2 == 206780
print('Tests passed.')
