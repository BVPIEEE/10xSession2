from string import ascii_lowercase
import random

class Anagrams:
	_file = open("words.txt", "r+")
	_list = []
	_WordMap = {}
	_WordToLen ={}
	_WorldLength = 6
	AnagramList = []

	def __init__(self):
		for i in self._file:
			i.lower()
			self._list.append(i.strip())

		for i in self._list:
			key = "".join(sorted(i))
			if key in self._WordMap:
				self._WordMap[key].append(i)
			else:
				self._WordMap[key]=[]
			
			length = len(i)
			if length in self._WordToLen:
				self._WordToLen[length].append(i)
			else:
				self._WordToLen[length]=[]
		pass

	def randomWord(self):
		while True:
			rand = random.randrange(3, self._WorldLength)
			word = random.choice(self._WordToLen[rand])
			if len(self._WordMap["".join(sorted(word))])<=1:
				continue
			else:
				self.getAnagrams(word)
				return word

	def getAnagrams(self, primeWord):
		for i in ascii_lowercase:
			word = primeWord+i
			key = "".join(sorted(word))
			if key in self._WordMap:
				if len(self._WordMap[key])!=0:
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
		if entry!= 'p':	
			if len(ana.AnagramList)!=0:
				if entry in ana.AnagramList:
					print("Correct Answer")
					ana.AnagramList.remove(entry)
				else:
					print("Wrong Answer try Again")
			else:
				print("You got it all right!!! Congratulations")
				break
		else:
			print("The Anagrams are:")
			print(ana.AnagramList)
			break
	print("Thanks for playing")