from time import sleep


class RepeatingStr:

	def __init__(self, _str):
		self._str = _str
		self.current = 0

	def __iter__(self):
		return self

	def __next__(self):
		index = self.current
		if index == len(self._str):
			index = 0
			self.current = 0
		else:
			self.current += 1
		return self._str[index]






foo = RepeatingStr('test')

for letter in foo:
	sleep(1)
	print(letter) 