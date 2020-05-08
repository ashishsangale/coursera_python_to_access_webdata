import re

sum = 0

data = open('regex.txt', 'r')
for line in data:
	num = re.findall('[0-9]+', line)
	if not num:
		continue
	else:
		for number in num:
			sum += int(number)


print(sum)