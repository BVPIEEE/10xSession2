from string import ascii_lowercase
import random

class Anagrams:
	_file = open("words.txt", "r+")
	_list = []
	_WordMap = {}
	_WordToLen ={}
	_WordLength = 5
	AnagramList = []

	def __init__(self):
		for i in self._file:
			i.lower()
			self._list.append(i.strip())
		
		for i in self._list:
			Word  = "".join(sorted(i))
			if Word in self._WordMap:
				self._WordMap[Word].append(i)
			else:
				self._WordMap[Word] = [i]

			length = len(i)
			if length in self._WordToLen:
				self._WordToLen[length].append(i)
			else:
				self._WordToLen[length] = []
		pass


	def randomWord(self):
		# You have to write your code here
		randomLength = random.randrange(3, self._WordLength)
		while True:
			if randomLength in self._WordToLen:
				word = random.choice(self._WordToLen[randomLength])
				key = "".join(sorted(word))
				if len(self._WordMap[key])<=1:
					continue
				else:
					self.getAnagrams(word)
					return word
		pass

	def getAnagrams(self, primeWord):
		for i in ascii_lowercase:
			word = primeWord + i
			key = "".join(sorted(word))
			if key in self._WordMap:
				if len(self._WordMap[key]) >0:
					self.AnagramList = self.AnagramList + self._WordMap[key]
				else:
					continue
			else:
				continue

if __name__ == "__main__":
	ana =Anagrams()
	print("Hello Welcome to the Anagrams Application")
	primeWord = ana.randomWord()
	print("\n The Word is :" + primeWord)
	print("Enter the Anagrams(Press 'q' to exit and Press 'p' to show anagrams) :")
	entry = ""
	while entry!='q':
		entry = input()
		if entry in ana.AnagramList:
			print("Correct You got it")
			ana.AnagramList.remove(entry)
		else:
			print("Wrong")

		if entry == 'p':
			print(ana.AnagramList)
	print("Thanks for playing")