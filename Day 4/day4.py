#
#
#
#:eyes:
#
#

with open('input.txt') as f:
  lines = f.read().strip().splitlines()

count = 0
for line in lines:
  a, b = line.split(',')
  lefta, righta = a.split('-')
  leftb, rightb = b.split('-')
  lefta, leftb, righta, rightb = int(lefta), int(leftb), int(righta), int(rightb)
  if lefta <= leftb and leftb <= righta\
  or leftb <= lefta and lefta <= rightb:
    count += 1
print(count)