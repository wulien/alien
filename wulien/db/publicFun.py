# -*- coding: utf-8 -*-
import re
import operDB
weatherStatic = {u'晴': 1, u'多云': 2, u'阴': 3, u'阵雨': 4, u'雷阵雨': 5, u'雷阵雨伴有冰雹': 6, u'雨夹雪': 7, u'小雨': 8,
		u'中雨': 9, u'大雨': 10, u'暴雨': 11, u'大暴雨': 12, u'特大暴雨': 13, u'阵雪': 14, u'小雪': 15, u'中雪': 16,
		u'大雪': 17, u'暴雪': 18, u'雾': 19, u'冻雨': 20, u'沙尘暴': 21, u'小雨转中雨': 22, u'中雨转大雨': 23, u'大雨转暴雨': 24,
		u'暴雨转大暴雨': 25, u'大暴雨转特大暴雨': 26, u'小雪转中雪': 27, u'中雪转大雪': 28, u'大雪转暴雪': 29, u'浮尘': 30, u'扬沙': 31,
		u'强沙尘暴': 32, u'霾': 33, u'晴转多云': 34, u'多云转阴': 35, u'阴转阵雨': 36, u'阴转小雨': 37}
windStatic = {u'微风': 1, u'东风3-4级': 2, u'东风3-4级转小于3级': 3, u'东风3-4级转5-6级': 4, u'东风5-6级转3-4级': 5, u'东风5-6级转7-8级': 6,
		u'东风7-8级转5-6级': 7, u'西风3-4级': 8, u'西风3-4级转小于3级': 9, u'西风3-4级转5-6级': 10, u'西风5-6级转3-4级': 11, u'西风5-6级转7-8级': 12,
		u'西风7-8级转5-6级': 13, u'南风3-4级': 8, u'南风3-4级转小于3级': 9, u'南风3-4级转5-6级': 10, u'南风5-6级转3-4级': 11, u'南风5-6级转7-8级': 12,
		u'南风7-8级转5-6级': 13,}
dressStatic = {u'炎热': 1, u'热': 2, u'暖': 3, u'舒适': 4, u'温凉': 5, u'气温较低': 6, u'冷': 7, u'温度极低': 8}
uvStatic = {u'最弱': 1, u'弱': 2, u'中等': 3, u'强': 4, u'最强': 5}
washCarStatic = {u'适宜': 1, u'较适宜': 2, u'较不宜': 3, u'不宜': 4}
travelStatic = {u'适宜': 1, u'较适宜': 2, u'一般': 3, u'较不宜': 4}
comfortableStatic = {u'舒适': 1, u'较为舒适': 2, u'不舒适': 3, u'很不舒适': 4, u'极不适应': 5}
exerciseStatic = {u'非常适宜': 1, u'适宜': 2, u'较适宜': 3, u'较不宜': 4, u'不宜': 5}
dryStatic = {u'非常适宜': 1, u'适宜': 2, u'较适宜': 3, u'不太适宜': 4, u'不适宜': 5}
allergyStatic = {u'极不易发': 1, u'不易发': 2, u'较不易发': 3, u'易发': 4, u'极易发': 5}

coninfo = ('127.0.0.1', 'root', 'vislecaina', 'weather')
basicInfoTableField = ('cityid', 'city', 'city_en', 'date_y', 'week', 'fchh')
temperatureTableField = ('temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6')
weatherTableField = ('weather1', 'weather2', 'weather3', 'weather4', 'weather5', 'weather6')
windTableField = ('wind1', 'wind2', 'wind3', 'wind4', 'wind5', 'wind6')
windLevelTableField = ('fx1', 'fx2', 'fl1', 'fl2', 'fl3', 'fl4', 'fl5', 'fl6')
otherInfoTableField = ('index', 'index48', 'index_uv', 'index48_uv', 'index_xc', 
			'index_tr', 'index_co', 'index_cl', 'index_ls', 'index_ag')

tableFields = (basicInfoTableField, temperatureTableField, weatherTableField, windTableField, otherInfoTableField)
tables = ('basicinfo', 'temperature', 'weather', 'wind', 'otherinfo')

def getFieldById(allInfo):
	tablesInfo = []
	cityid = allInfo['cityid']
	if (len(tableFields) < 6):
		print "Tables less than expect! Error------"
	basicInfoField = tableFields[0]
	basicInfoTableValues = []
	for field in basicInfoField:
		value = allInfo[field]
		basicInfoTableValues.append(value)
	basicinfo = convertForShow(basicInfoTableValues)
	tablesInfo.append(basicinfo)
	#delete table(basicinfo)
	db = operDB.DBOperation()
	db.deleteRowInTable(tables[0], cityid)

	temperatureField = tableFields[1]
	#Get yesterday temperature first
	row = getYesterdayTemp(db, cityid)
	temperatureTableValues = []
	temperatureTableValues.append(cityid)
	temperatureTableValues.append(row[0])
	temperatureTableValues.append(row[1])
	for field in temperatureField:
		value = allInfo[field].encode('gbk')
		tempHighAndLow = re.split('~', value)
		if (len(tempHighAndLow) == 2):
			tempHigh = tempHighAndLow[0][ : -2]
			tempLow = tempHighAndLow[1][ : -2]
			temperatureTableValues.append(tempHigh)
			temperatureTableValues.append(tempLow)
	temperature = convertForShow(temperatureTableValues)
	tablesInfo.append(temperature)

	weatherField = tableFields[2]
	weatherTableValues = []
	weatherTableValues.append(cityid)
	weaTable = tables[2]
	row = db.getYesterdayWeather(weaTable, cityid)
	if (0 == len(row)):
		yesWeather = 100
	else:
		yesWeather = row[0]
	weatherTableValues.append(yesWeather)
	for field in weatherField:
		value = allInfo[field]
		print type(value)
		print value
		try:
			value = weatherStatic[value]
		except KeyError:
			print value
			value = 100
		weatherTableValues.append(value)
	weather = convertForShow(weatherTableValues)
	tablesInfo.append(weather)
	#delete table(weather)
	db.deleteRowInTable(tables[2], cityid)

	windField = tableFields[3]
	windTableValues = []
	windTableValues.append(cityid)
	windTable = tables[3]
	row = db.getYesterdayWind(windTable, cityid)
	if (0 == len(row)):
		yesWind = 100
	else:
		yesWind = row[0]
	windTableValues.append(yesWind)
	for field in windField:
		value = allInfo[field]
		print type(value)
		print value
		try:
			value = windStatic[value]
		except KeyError:
			print value
			value = 100
		windTableValues.append(value)
	wind = convertForShow(windTableValues)
	tablesInfo.append(wind)
	#delete table(weather)
	db.deleteRowInTable(tables[3], cityid)

	return tablesInfo


def getYesterdayTemp(db, cityid):
	table = tables[1]
	yesData = db.getYesTempByCityId(table, cityid)
	#delete datas of yesterday
	db.deleteRowInTable(table, cityid)
	return yesData

def convertForShow(tableValues):
	tmp = ''
	i = 0
	while(i < len(tableValues)):
		item = tableValues[i]
		if ('str' == type(item)):
			item = str(item).encode('gbk')
		if len(tableValues) - 1 == i:
			tmp += '\'%s\'' % item
		else:
			tmp += '\'%s\', ' % item
		i += 1
	tmp = '(' + tmp + ')'

	return tmp

# if __name__ == '__main__':
# 	c = u''
# 	c = c.encode('utf-8')
# 	print c
# 	print type(c)
# 	b = []
# 	b.append(c)
# 	b.append(c)
# 	tmp = ''
# 	i = 0
# 	while(i < len(b)):
# 		if len(b) - 1 == i:
# 			tmp += '%s' % b[i]
# 		else:
# 			tmp += '%s, ' % b[i]
# 		i += 1
# 	print type(tmp)
# 	print tmp
	
# 	f = open('temp.txt', 'w')
# 	f.write(tmp)
# 	f.close()