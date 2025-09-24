# TextEditor实现以下功能：append, backspace, undo, redo, select, bold. input长这样：String[][] input
# append: 在当前字符串结尾append或将选中的字符串replace e.g. ["1", "APPEND", "hello"]
# backspace: 删掉当前字符串最后一位或选中的字符串 e.g. ["2", "BACKSPACE"]
# undo: 撤销上一步操作 e.g. ["3", "UNDO"]
# redo: 把上一步被撤销的操作重做 e.g. ["4", "REDO"]
# select: 选中当前字符串的某一部分, 给定了[start, end)  e.g. ["5", "SELECT", 3, 6]
# bold: 将选中的字符串bold e.g. ["6", "BOLD"]
class TextEditor():
	def __init__(self, input):
		self.input = input
		self.output = []
		self.history = []
		self.forUndo = []
		self.select = []

	def textEditor(self):
		sortedByTime = sorted(self.input, key = lambda x:x[0])
		for instruction in sortedByTime:
			if instruction[1] == 'APPEND':
				if self.select and len(self.output) > 0:
					last = self.output.pop()
					newLast = last[:self.select[0]] + instruction[2] + last[self.select[1]:]
					self.output.append(newLast)
				else:
					self.output.append(instruction[2])
					self.forUndo.append([instruction[2],'APPEND'])
					self.history = []

				
			elif instruction[1] == 'BACKSPACE':
				if len(self.output) > 0:
					last = self.output.pop()
					self.forUndo.append([last,'BACKSPACE'])
					if self.select:
						
						start = self.select[0]
						end = self.select[1]
						newLast = last[:start] + last[end:]
						self.output.append(newLast)

					else:
						
						newLast = last[:-1]
						if len(newLast) > 0:
							self.output.append(newLast)
			
			elif instruction[1] == 'UNDO':
				if len(self.forUndo) > 0:
					currentUndo = self.forUndo.pop()
					
					if currentUndo[1] == 'APPEND':
						self.output.pop()
						self.history.append(currentUndo)
					elif currentUndo[1] == 'BACKSPACE':
						if len(self.output) > 0:
							saveHistoy = self.output.pop()
							self.output.append(currentUndo[0])
							currentUndo[0] = saveHistoy
							self.history.append(currentUndo)


			elif instruction[1] == 'REDO':
				if len(self.history) > 0:
					currentRedo = self.history.pop()
					if currentRedo[1] == 'APPEND':
						self.output.append(currentRedo[0])
					elif currentRedo[1] == 'BACKSPACE':
						if(len(self.output) > 0):
							self.output.pop()
							self.output.append(currentRedo[0])

			elif instruction[1] == 'SELECT':
				
				start, end = instruction[2], instruction[3]
				self.select = [start, end]
			elif instruction[1] == 'BOLD':
				if self.select:
					current = self.output.pop()
					start = self.select[0]
					end = self.select[1]
					newCurrent = current[:start]+'*'+ current[start:end] + '*' + current[end:]
					self.output.append(newCurrent)

		return ''.join(self.output)

T = TextEditor(
	[["0","APPEND","Hello"], 
 ["1","SELECT",1,6], 
 ["2","BOLD"]])
print(T.textEditor())

				





