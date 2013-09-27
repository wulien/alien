# -*- coding=utf-8 -*-
import scrap
import readXml
import publicFun
import operDB
import sys

coninfo = ('127.0.0.1', 'root', 'vislecaina', 'weather')
basicInfoTableField = ('cityid', 'city', 'city_en', 'date_y', 'week', 'fchh')
temperatureTableField = ('temp1', 'temp2', 'temp3', 'temp4', 'temp5')
weatherTableField = ('weather1', 'weather2', 'weather3', 'weather4', 'weather5')
windTableField = ('wind1', 'wind2', 'wind3', 'wind4', 'wind5')
windLevelTableField = ('fx1', 'fx2', 'fl1', 'fl2', 'fl3', 'fl4', 'fl5', 'fl6')
otherInfoTableField = ('index', 'index_d', 'index48', 'index48_d', 'index_uv', 'index48_uv', 'index_xc', 
			'index_tr', 'index_co', 'index_cl', 'index_ls', 'index_ag')

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
	