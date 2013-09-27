import requests
import json
import urllib2

class weatherScrap(object):
	def __init__(self, url):
		self.url = url
		print "-----The url you input is \"%s\"-----" % self.url

	def getWeatherInfo(self):
		try:
			weatherReq = urllib2.urlopen(self.url)
		except:
			print "Error occur getting %s datas" % self.url
		try:
			allInfo = json.load(weatherReq)
			allInfo = allInfo['weatherinfo']
		except:
			print "Parse json error!"
			allInfo = []
		print "-----Get weather datas OK!-----"
		return allInfo

	def getInfoById(self, id):
		allInfo = self.getWeatherInfo()
		info = allInfo[id]
		print type(info)
		info = info.encode('UTF-8')
		return info


if __name__ == '__main__':
	url = "http://m.weather.com.cn/data/101200101.html"
	info = weatherScrap(url)
	info.getInfoById('index_d')
