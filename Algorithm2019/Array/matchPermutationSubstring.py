def isMatch(m1, m2):
		for k in range(26):
			if m1[k] != m2[k]:
				return False

		return True
def matchPermutationSubstring(sub, string):

	mapSub = [0] * 26
	mapString = [0] * 26

	for i in range(len(sub)):
		mapSub[ord(sub[i])-ord('a')] += 1
		mapString[ord(string[i])-ord('a')] += 1

	lenSub = len(sub)
	lenString = len(string)

	for j in range(lenString-lenSub):
		if isMatch(mapSub, mapString):
			return True

		mapString[ord(string[j+len(sub)])-ord('a')] += 1
		mapString[ord(string[j])-ord('a')] -= 1

	return False


	


# print(matchPermunateSubstring('ab','abcdfe'))


# // function isMatch(m1,m2){
# // 	return JSON.stringify(a)==JSON.stringify(b)
# // }

	
# // sub = 'cd'
# // str = 'abcdf'

# // function matchPermutationSubstring(sub, str){
# // 	mapSub = Array(26).fill(0);[0,0..]
# // 	mapStr = Array(26).fill(0); [1,1..]
# // 	lenSub = sub.length
# // 	lenString = str.length
# // 	for(let i=0; i<lenSub;i++){
# // 		mapSub[sub.charCodeAt(i)-97] += 1
# // 		mapStr[str.charCodeAt(i)-97] += 1
# // 	}
# // 	for(let j=0; j < (lenString-lenSub); j++) {
# // 		if(isMatch(mapSub,mapStr)){
# // 			return True
# // 		}
# // 		else {
# // 			mapStr[str.charCodeAt(j+lenSub)-97] += 1
# // 			mapStr[str.charCodeAt(j)-97] -= 1
# // 		}
# // 	}
# // 	return false

# // }


