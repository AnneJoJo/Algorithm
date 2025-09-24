def hourse(hourse):
 	gym = [0]*len(hourse)
 	school = [0]*len(hourse)
 	store = [0]*len(hourse)
 	for i in range(len(hourse)):
 		if hourse[i].get('gym'):
 			gym[i] = 1
 		if hourse[i].get('school'):
 			school[i] = 1
 		if hourse[i].get('store'):
 			store[i] = 1
 	# get all position of each falility 
 	farthest = [0] * len(hourse)
 	gymDist = getDistance(gym)
 	storeDist =getDistance(store)
 	schoolDist = getDistance(school)
 	print(gymDist, storeDist, schoolDist)
 	for k in range(len(hourse)):
 		farthest[k] = max(gymDist[k],storeDist[k],schoolDist[k])
 	print('The block is:',farthest.index(min(farthest)))
 	return farthest.index(min(farthest))

def getDistance(arr):
 	steps = [0] * len(arr)
 	for j in range(len(arr)):
 		
 		if arr[j] == 0:
 			step = 1
 			left = j - 1
 			right = j + 1
 			while left >=0 or right < len(arr):
 				if (left >=0 and arr[left] == 1) or (right < len(arr) and arr[right] == 1):
 					steps[j] = step
 					break
 				else:
 					left -= 1
 					right += 1
 					step += 1
 	return steps

 				
block = [
 	{'school': True,
 	 'store': False,
 	 'gym': False
 	},
 	{'school': False,
 	 'store': False,
 	 'gym': True
 	},
 	{'school': True,

 	 'store': False,
 	 'gym': True
 	},
 	{'school': True,
 	 'store': False,
 	 'gym': False
 	},
 	{'school': True,

 	 'store': True,
 	 'gym': False
 	}

 ]
print(hourse(block))















