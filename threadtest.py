import thread
import time
c=1
def funt(no,a):	
	global c
	while True:
		time.sleep(1)
		c=c+1
		print 'thread no %d =%d ,'%(no,c)

def test():
	thread.start_new_thread(funt,(1,2))
	thread.start_new_thread(funt,(2,2))
	thread.start_new_thread(funt,(3,3))
	time.sleep(20)
if __name__=='__main__':
	test()
