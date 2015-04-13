import os
def myfork():
	pid=os.fork()
	if pid==0:
		print "this is child %d-----%d" % (pid,os.getpid())
	else:
		print "this is parent %d-----%d" % (pid,os.getpid())
if __name__=='__main__':
	myfork()
