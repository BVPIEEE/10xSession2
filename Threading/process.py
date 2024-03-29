from threading import Thread
from queue import Queue
import time

class Process:
	def __init__(self):
		self.stopped = False
		self.Q = Queue(maxsize = 128)
		self.thread = Thread(target =self.returnNumber, args=())
		self.thread.daemon = True
	def start(self):
		self.thread.start()
		return self

	def returnNumber(self):
		if self.stopped:
			return
		else:
			while True:
				if self.Q.qsize() >0:
					value = self.Q.get()
					print("Hello the output is "+ str(value))
				else:
					time.sleep(0.5)

	def putInQ(self, number):
		self.Q.put(number)
		return self

	def stop(self):
		self.stopped == True
		self.thread.join()
		return self
