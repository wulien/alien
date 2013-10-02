# -*- coding=utf-8 -*-
import scrap
import readXml
import publicFun
import operDB
import sys


def go(codes):
	db = operDB.DBOperation()
	for code in codes:
		cururl = url + code.strip('\n') + '.html'
		print "-----Get %s datas-----" % cururl
		myScrap = scrap.weatherScrap(cururl)
		allInfo = myScrap.getWeatherInfo()
		if 0 == len(allInfo) :
			continue
		tablesInfo = publicFun.getFieldById(allInfo)
		for i in range(len(tablesInfo)):
			db.insertData(tablesInfo[i], publicFun.tables[i])
			db.readTable(publicFun.tables[i])

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	url = "http://m.weather.com.cn/data/"
	codeXml = readXml.ReadXml('cityAndCode.xml')
	codes = codeXml.getAllCodes()
	go(codes)
	