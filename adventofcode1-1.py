inputFile = open('aoc1-1-input.txt','r')
depthChart = inputFile.readlines()
increaseCount = 0
prevDepth = 0
i=0
for line in depthChart:
	depth = int(line.strip().split(':')[0])
#	print('iteration: ',i)
#	print('depth: ',depth)
	if(i>0):
		prevDepth = depthChart[i-1]
#		print('previous depth: ',prevDepth)
		if(int(depth) > int(prevDepth)):
			increaseCount += 1
#			print('increased ',increaseCount,' times')
	i += 1
inputFile.close()
print('puzzle solution: ',increaseCount,' increases')