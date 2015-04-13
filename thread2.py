import threading
import time
mylock=threading.RLock()
count=0
class aa(threading.Thread):
	def __init__(self,no,interval):
		threading.Thread.__init__(self)
		self.no=no
		self.interval=interval
		self.isstop=False
	def run(self):
		global count
		a=0
		while a<10:
			mylock.acquire()
			count+=1
	
			mylock.release()
	
			print 'thread %d==%d' %(self.no,count)
			time.sleep(self.interval)
			a+=1
	def stop(self):
		self.isstop=True
def factory():
	t1=aa(1,2)
	t1.start()
	t2=aa(2,2)
	t2.start()
	time.sleep(20)
	t1.stop()
if __name__=="__main__":
	factory()
