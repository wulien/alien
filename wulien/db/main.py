# -*- coding=utf-8 -*-
import scrap
import readXml
import publicFun
import operDB
import sys

coninfo = ('127.0.0.1', 'root', 'vislecaina', 'weather')
basicInfoTableField = ('cityid', 'city', 'city_en', 'date_y', 'week', 'fchh')


def go(codes):
	db = operDB.DBOperation(coninfo)
	db.deleteTable()
	for code in codes:
		cururl = url + code.strip('\n') + '.html'
		print "-----Get %s datas-----" % cururl
		myScrap = scrap.weatherScrap(cururl)
		allInfo = myScrap.getWeatherInfo()
		if 0 == len(allInfo) :
			continue
		basicinfo = publicFun.getFieldById(allInfo, basicInfoTableField)
		basicInfoTable = 'basicinfo'
		db.insertData(basicinfo, basicInfoTable)
	db.readTable(basicInfoTable)

if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf-8')
	url = "http://m.weather.com.cn/data/"
	codeXml = readXml.ReadXml('cityAndCode.xml')
	codes = codeXml.getAllCodes()
	go(codes)
	