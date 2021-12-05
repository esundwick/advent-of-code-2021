inputFile = open('aoc1-1-input.txt','r')
depthChart = inputFile.readlines()
increaseCount = 0
prevTotal = 0
depthWindow = []
i=0
countStop = len(depthChart)-2
# print('stop at ',countStop,' iterations')
for line in depthChart:
	while(i < countStop):
		prevTotal = sum(depthWindow)
		depthWindow = [int(depthChart[i].strip().split(':')[0]), int(depthChart[i+1].strip().split(':')[0]), int(depthChart[i+2].strip().split(':')[0])]
		windowTotal = sum(depthWindow)
#		print('iteration: ',i)
#		print('depth window: ',depthWindow)
#		print('window sum: ',windowTotal,'previous measurement: ',prevTotal)
		if(i>0):
			if(windowTotal > prevTotal):
				increaseCount += 1
#				print('depth increased!')
		i += 1
inputFile.close()
print('puzzle solution: ',increaseCount,' increases')