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
		# You have to write your code here
		pass

	def randomWord(self):
		# You have to write your code here
		pass

	def getAnagrams(self, primeWord):
		# You have to write your code here
		pass

if __name__ == "__main__":
	ana =Anagrams()
	print("Hello Welcome to the Anagrams Application")
	# primeWord = ana.randomWord()
	# print("\n The Word is :" + primeWord)
	print("Enter the Anagrams(Press 'q' to exit and Press 'p' to show anagrams) :")
	entry = ""
	while entry!='q':
		entry = input()
		# You have to write your code here
	print("Thanks for playing")