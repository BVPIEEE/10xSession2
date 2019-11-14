from process import Process
import time

if __name__ == "__main__":
	p=Process()
	p=p.start()
	i = 10
	while i:
		i = int(input("Enter the number"))
		p.putInQ(i)
		time.sleep(0.1)
	p.stop()