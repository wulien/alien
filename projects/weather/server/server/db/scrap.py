import requests
import json
import urllib2
import log

class weatherScrap(object):
	def __init__(self, url):
		self.url = url
		strLog = "The url you input is \"%s\"" % self.url
		log.log(strLog)

	def getWeatherInfo(self):
		for i in range(5):
			try:
				weatherReq = urllib2.urlopen(self.url)
				break;
			except:
				strLog = "Error occur getting %s datas" % self.url
				log.log(strLog)
				strLog = "Trying %d times" % i
				log.log(strLog)
		try:
			allInfo = json.load(weatherReq)
			allInfo = allInfo['weatherinfo']
		except:
			strLog = "Parse json error!"
			log.log(strLog)
			allInfo = []
		strLog = "Get weather datas OK"
		log.log(strLog)
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
