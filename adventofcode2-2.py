inputFile = open('aoc2-1-input.txt','r')
directions = inputFile.readlines()
sub_pos = {
	'distance':0,
	'aim':0,
	'depth':0
}
for line in directions:
#	print('sub distance: ',sub_pos['distance'])
#	print('sub aim: ', sub_pos['aim'])
#	print('sub depth: ',sub_pos['depth'])
#	print('')
	length = len(line.strip())
	x = int(line[length-1])
#	print(line.strip())
	if "down" in line:
		sub_pos['aim'] += x
	elif "up" in line:
		sub_pos['aim'] -= x
	elif "forward" in line:
		sub_pos['distance'] += x
		sub_pos['depth'] += sub_pos['aim']*x
	else:
		print("no direction found in line")


#	print()
inputFile.close()
print('final distance: ', sub_pos['distance'])
print('final depth: ', sub_pos['depth'])

puzzle_output = int(sub_pos['distance'])*int(sub_pos['depth'])

print('Puzzle solution: ',puzzle_output)