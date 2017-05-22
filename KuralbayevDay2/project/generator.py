
from random import randint

with open('g1.txt', 'w') as file:

	for i in range(0, 100):
		num = randint(0, 100)
		file.write(str(num) + '\n')


