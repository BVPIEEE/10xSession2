from threading import Thread

def printUpto10():
	for i in range(1,11):
		print(i)

def printUpto20():
	for i in range(10,21):
		print(i)		
if __name__ == "__main__":
	thread1 = Thread(target = printUpto10, args = ())
	thread2 = Thread(target = printUpto20, args = ())
	thread1.start()
	thread2.start()
	thread1.join()
	thread2.join()