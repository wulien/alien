# -*- coding: utf-8 -*-
import time
# class log(object):
# 	def __init__(self):
# 		fileName = 'log/' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt'
# 		try:
# 			self.f = open(fileName, 'w+')
# 		except:
# 			print "Open file Error..."
# 	def __del__(self):
# 		try:
# 			self.f.close()
# 		except:
# 			print "No file opened..."

# 	def writeStr(self, strIn):
# 		currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n'
# 		print currentTime
# 		self.f.write(currentTime)
# 		strIn += '\n'
# 		self.f.write(strIn)

def log(strIn):
	fileName = 'log/' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.txt'
	try:
		f = open(fileName, 'a+')
	except:
		print "Open file Error..."
	currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '\n'
	print currentTime
	f.write(currentTime)
	strIn += '\n'
	f.write(strIn)
	f.write("\n")
	try:
		f.close()
	except:
		print "No file opened..."

