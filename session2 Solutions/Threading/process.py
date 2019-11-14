from threading import Thread
from Queue import Queue
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
			return self
		else:
			while True:
				if self.Q.qsize():
					time.sleep(0.1)
				elif self.stopped:
					self.thread.join()
					return self
				else:
					print("The square number is:",self.Q.get()**2)

	def putInQ(self, number):
		self.Q.put(number)
		return self

	def stop(self):
		self.stopped==True
		return self
