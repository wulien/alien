# -*- coding=utf-8 -*-
import scrap
import readXml
import publicFun
import operDB
import sys
import log


def go(codes):
	db = operDB.DBOperation()
	todayUrl = "http://m.weather.com.cn/data/"
	for code in codes:
		url = todayUrl + code.strip('\n') + '.html'
		log.log("------------------------------------start------------------------------------------")
		strLog = "Getting %s datas;" % url
		log.log(strLog)
		print strLog
		myScrap = scrap.weatherScrap(url)
		allInfo = myScrap.getWeatherInfo()
		if 0 == len(allInfo) :
			continue
		tablesInfo = publicFun.getFieldById(allInfo)
		for i in range(len(tablesInfo)):
			db.insertData(tablesInfo[i], publicFun.tables[i])
	for i in range(len(tablesInfo)):
		db.readTable(publicFun.tables[i])
	#deal current weather
	currentUrl = "http://www.weather.com.cn/data/sk/"
	db.deleteTable('currentweather')
	for code in codes:
		url = currentUrl + code.strip('\n') + '.html'
		myScrap = scrap.weatherScrap(url)
		allInfo = myScrap.getWeatherInfo()
		if 0 == len(allInfo) :
			continue
		currentweather = publicFun.getCurrentTableField(allInfo)
		db.insertData(currentweather, 'currentweather')
	db.readTable('currentweather')


if __name__ == '__main__':
# 	reload(sys)
# 	sys.setdefaultencoding('utf-8')
	codeXml = readXml.ReadXml('cityAndCode.xml')
	codes = codeXml.getAllCodes()
	go(codes)
	