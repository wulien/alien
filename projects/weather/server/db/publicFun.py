# -*- coding: utf-8 -*-
import re
import operDB
import log
weatherStatic = {u'晴': 1, u'多云': 2, u'阴': 3, u'阵雨': 4, u'雷阵雨': 5, u'雷阵雨伴有冰雹': 6, u'雨夹雪': 7, u'小雨': 8,
		u'中雨': 9, u'大雨': 10, u'暴雨': 11, u'大暴雨': 12, u'特大暴雨': 13, u'阵雪': 14, u'小雪': 15, u'中雪': 16,
		u'大雪': 17, u'暴雪': 18, u'雾': 19, u'冻雨': 20, u'沙尘暴': 21, u'小雨转中雨': 22, u'中雨转大雨': 23, u'大雨转暴雨': 24,
		u'暴雨转大暴雨': 25, u'大暴雨转特大暴雨': 26, u'小雪转中雪': 27, u'中雪转大雪': 28, u'大雪转暴雪': 29, u'浮尘': 30, u'扬沙': 31,
		u'强沙尘暴': 32, u'霾': 33, u'晴转多云': 34, u'多云转阴': 35, u'阴转阵雨': 36, u'阴转小雨': 37, u'阴转晴': 38, u'晴转阴': 39,
		u'阴转多云': 40, u'大雨转中雨': 41, u'阵雨转晴': 42, u'阵雨转小雨': 43, u'小雨转多云': 44, u'小雨转暴雨': 45, u'多云转小雨': 46, u'小雨转大雨': 47,
		u'多云转晴': 48, u'晴转暴雨': 49, u'小雨转特大暴雨': 50, u'多云转阵雨': 51, u'阵雨转阴': 52, u'阵雨转多云': 53, u'小雨转阴': 54, u'雨夹雪转多云': 55
		, u'小到中雨': 56, u'中雨转小雨': 57, u'中雨转多云': 58, u'晴转小雨': 59, u'小雨转晴': 60, u'雨夹雪转阵雨': 61, u'小雨转阵雨': 62, u'多云转雨夹雪': 63, 
		u'阵雪转多云': 64, u'阵雪转多云': 65, u'小到中雨转阵雨': 66, u'晴转中雨': 67, u'晴转雨夹雪': 68, u'晴转阵雨': 69, u'雨夹雪转阵雪': 70, u'小雨转雨夹雪': 71,
		u'小雪转晴': 72, u'晴转小雪': 73, u'小雪转雨夹雪': 74, u'雨夹雪转小雨':75, u'小雪转多云': 76, u'雨夹雪转小雪': 77}
windStatic = {u'微风': 1, u'东风3-4级': 2, u'东风3-4级转小于3级': 3, u'东风3-4级转5-6级': 4, u'东风5-6级转3-4级': 5, u'东风5-6级转7-8级': 6,
		u'东风7-8级转5-6级': 7, u'西风3-4级': 8, u'西风3-4级转小于3级': 9, u'西风3-4级转5-6级': 10, u'西风5-6级转3-4级': 11, u'西风5-6级转7-8级': 12,
		u'西风7-8级转5-6级': 13, u'南风3-4级': 14, u'南风3-4级转小于3级': 15, u'南风3-4级转5-6级': 16, u'南风5-6级转3-4级': 17, u'南风5-6级转7-8级': 18,
		u'南风7-8级转5-6级': 19, u'微风转东南风3-4级': 20, u'东南风3-4级转4-5级': 21, u'东南风3-4级转南风4-5级': 22, u'东北风5-6级': 23, u'东北风转北风3-4级': 24,
		u'东北风转西北风3-4级': 25, u'东风转西风3-4级': 26, u'东南风转东北风3-4级': 27, u'西南风小于3级转南风3-4级': 28, u'东南风小于3级转北风3-4级': 29,
		u'北风小于3级转南风3-4级': 30, u'南风小于3级转4-5级': 31, u'微风转东北风3-4级': 32, u'东南风小于3级转西风3-4级': 33, u'东风小于3级转东北风3-4级': 34,
		u'东南风小于3级转东风3-4级': 35, u'西风转南风3-4级': 36, u'西南风转北风3-4级': 37, u'北风转西南风3-4级': 38, u'西北风小于3级转西风4-5级': 39,
		u'西风小于3级转南风3-4级': 40, u'南风小于3级转东风3-4级': 41, u'东风小于3级转南风3-4级': 42, u'东风小于3级转东南风3-4级': 43, u'东风小于3级转北风3-4级': 44,
		u'南风小于3级转西风3-4级': 45, u'西南风转东风3-4级': 46, u'东风转北风3-4级': 47, u'西风小于3级转西南风3-4级': 48, u'东风3-4级转西风小于3级': 49,
		u'西南风3-4级转小于3级': 50, u'东南风小于3级转南风3-4级': 51, u'西风转西南风小于3级': 52, u'东北风小于3级转西南风3-4级': 53, u'东北风小于3级转西北风3-4级': 54,
		u'南风小于3级转西南风3-4级': 55, u'西南风转北风4-5级': 56, u'西南风3-4级转4-5级': 57, u'南风转西南风4-5级': 58, u'北风转西南风4-5级': 59}
dressStatic = {u'炎热': 1, u'热': 2, u'暖': 3, u'舒适': 4, u'温凉': 5, u'气温较低': 6, u'冷': 7, u'温度极低': 8}
uvStatic = {u'最弱': 1, u'弱': 2, u'中等': 3, u'强': 4, u'最强': 5}
washCarStatic = {u'适宜': 1, u'较适宜': 2, u'较不宜': 3, u'不宜': 4}
travelStatic = {u'适宜': 1, u'较适宜': 2, u'一般': 3, u'较不宜': 4}
comfortableStatic = {u'舒适': 1, u'较为舒适': 2, u'不舒适': 3, u'很不舒适': 4, u'极不适应': 5}
exerciseStatic = {u'非常适宜': 1, u'适宜': 2, u'较适宜': 3, u'较不宜': 4, u'不宜': 5}
dryStatic = {u'非常适宜': 1, u'适宜': 2, u'较适宜': 3, u'不太适宜': 4, u'不适宜': 5}
allergyStatic = {u'极不易发': 1, u'不易发': 2, u'较不易发': 3, u'易发': 4, u'极易发': 5}
otherinfoStatic = {u'炎热': 1, u'热': 2, u'舒适': 3, u'较舒适': 4, u'较冷': 5, u'冷': 6, u'寒冷': 7, u'温度极低': 8,
		u'最弱': 9, u'弱': 10, u'中等': 11, u'强': 12, u'最强': 13, u'一般': 14, u'舒适': 15, u'较为舒适': 16, u'不舒适': 17, u'很不舒适': 18, u'极不适应': 19,
		u'非常适宜': 20, u'适宜': 21, u'不太适宜': 22, u'不适宜': 23, u'极不易发': 24, u'不易发': 25, u'较不易发': 26, u'易发': 27, u'极易发': 28}

windDirectionStatic ={u'东风': 1, u'西风': 2, u'南风': 3, u'北风': 4, u'东北风': 5, u'东南风': 6, u'西北风': 7, u'西南风': 8,
			u'偏东风': 9, u'偏南风': 10, u'偏西风': 11, u'偏北风': 12}

weekStatic = {u'星期一': 1, u'星期二': 2, u'星期三': 3, u'星期四': 4, u'星期五': 5, u'星期六': 6, u'星期日': 7}


coninfo = ('127.0.0.1', 'root', 'vislecaina', 'weather')
basicInfoTableField = ('cityid', 'city', 'city_en', 'date_y', 'week', 'fchh')
temperatureTableField = ('temp1', 'temp2', 'temp3', 'temp4', 'temp5', 'temp6')
weatherTableField = ('weather1', 'weather2', 'weather3', 'weather4', 'weather5', 'weather6')
windTableField = ('wind1', 'wind2', 'wind3', 'wind4', 'wind5', 'wind6')
windLevelTableField = ('fx1', 'fx2', 'fl1', 'fl2', 'fl3', 'fl4', 'fl5', 'fl6')
otherInfoTableField = ('index', 'index48', 'index_uv', 'index48_uv', 'index_xc', 
			'index_tr', 'index_co', 'index_cl', 'index_ls', 'index_ag')
currentWeatherTabelField = ('cityid', 'city', 'temp', 'WD', 'WS', 'SD', 'WSE', 'time')

tableFields = (basicInfoTableField, temperatureTableField, weatherTableField, windTableField, otherInfoTableField)
tables = ('basicinfo', 'temperature', 'weather', 'wind', 'otherinfo')

def getFieldById(allInfo):
	tablesInfo = []
	cityid = allInfo['cityid']
	if (len(tableFields) < 5):
		strLog = "Tables less than expect! Error"
		log.log(strLog)
		print strLog
	basicInfoField = tableFields[0]
	basicInfoTableValues = []
	for field in basicInfoField:
		try:
			value = allInfo[field]
			if ('week' == field):
				try:
					value = weekStatic[value]
				except:
					tempStr = value.encode('gbk')
					strLog = "Error in basicinfo ! Can't find value = %s" % tempStr
					print strLog
					log.log(strLog)
					value = 100
		except:
			value = '100'
			strLog = "KeyError %s, cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		basicInfoTableValues.append(value)
	strLog = "Getting table \'%s\' data, cityid = %s" % (tables[0], cityid)
	log.log(strLog)
	print strLog
	basicinfo = convertForShow(basicInfoTableValues)
	tablesInfo.append(basicinfo)
	#delete table(basicinfo)
	strLog = "Deleting table %s, cityid = %s" % (tables[0], cityid)
	log.log(strLog)
	print strLog
	db = operDB.DBOperation()
	db.deleteRowInTable(tables[0], cityid)

	temperatureField = tableFields[1]
	#Get yesterday temperature first
	strLog = 'Getting yesterday temperature'
	log.log(strLog)
	row = getYesterdayTemp(db, cityid)
	temperatureTableValues = []
	temperatureTableValues.append(cityid)
	temperatureTableValues.append(row[0])
	temperatureTableValues.append(row[1])
	for field in temperatureField:
		try:
			value = allInfo[field].encode('gbk')
		except:
			value = '100'
			strLog = "Error field = %s ,cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		tempHighAndLow = re.split('~', value)
		if (len(tempHighAndLow) == 2):
			tempHigh = tempHighAndLow[0][ : -2]
			tempLow = tempHighAndLow[1][ : -2]	
		else:
			tempHigh = 100
			tempLow = 100
		temperatureTableValues.append(tempHigh)
		temperatureTableValues.append(tempLow)
	strLog = "Getting table \'%s\' data, cityid = %s" % (tables[1], cityid)
	log.log(strLog)
	print strLog
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
		try:
			value = allInfo[field]
			try:
				value = weatherStatic[value]
			except KeyError:
				tempStr = value.encode('gbk')
				strLog = "KeyError in weatherStatic ! Can't find value = %s" % tempStr
				print strLog
				log.log(strLog)
				value = 100
		except:
			value = 100
			strLog = "Error field = %s ,cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		weatherTableValues.append(value)
	strLog = "Getting table \'%s\' data, cityid = %s" % (tables[2], cityid)
	log.log(strLog)
	weather = convertForShow(weatherTableValues)
	tablesInfo.append(weather)
	#delete table(weather)
	strLog = "Deleting table %s, cityid = %s" % (tables[2], cityid)
	log.log(strLog)
	db.deleteRowInTable(tables[2], cityid)

	windField = tableFields[3]
	windTableValues = []
	windTableValues.append(cityid)
	windTable = tables[3]
	strLog = 'Getting yesterday wind'
	log.log(strLog)
	row = db.getYesterdayWind(windTable, cityid)
	if (0 == len(row)):
		yesWind = 100
	else:
		yesWind = row[0]
	windTableValues.append(yesWind)
	for field in windField:
		try:
			value = allInfo[field]
			try:
				value = windStatic[value]
			except KeyError:
				strLog = "KeyError in windStatic ! Can't find value = %s" % value
				print strLog
				log.log(strLog)
				value = 100
		except:
			value = 100
			strLog = "Error field = %s ,cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		windTableValues.append(value)
	strLog = "Getting table \'%s\' data, cityid = %s" % (tables[3], cityid)
	log.log(strLog)
	print strLog
	wind = convertForShow(windTableValues)
	tablesInfo.append(wind)
	#delete table(weather)
	db.deleteRowInTable(tables[3], cityid)

	otherinfoField = tableFields[4]
	otherinfoTableValues = []
	otherinfoTableValues.append(cityid)
	for field in otherinfoField:
		try:
			value = allInfo[field] 
			try:
				value = otherinfoStatic[value]
			except KeyError:
				strLog = "KeyError in otherinfoStatic ! Can't find value = %s" % value
				print strLog
				log.log(strLog)
				value = 100
		except:
			value = 100
			strLog = "Error field = %s ,cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		otherinfoTableValues.append(value)
	strLog = "Getting table \'%s\' data, cityid = %s" % (tables[4], cityid)
	log.log(strLog)
	print strLog
	otherinfo = convertForShow(otherinfoTableValues)
	tablesInfo.append(otherinfo)
	db.deleteRowInTable(tables[4], cityid)

	return tablesInfo


def getYesterdayTemp(db, cityid):
	table = tables[1]
	yesData = db.getYesTempByCityId(table, cityid)
	#delete datas of yesterday
	strLog = "Deleting table \'%s\' data, cityid = %s" % (tables[1], cityid)
	log.log(strLog)
	print strLog
	db.deleteRowInTable(table, cityid)
	strLog = "Delete OK"
	log.log(strLog)
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
	strLog = tmp.encode('gbk')
	log.log(strLog)
	return tmp

def getCurrentTableField(allInfo):
	currentWeatherTableValues = []
	cityid = allInfo['cityid']
	for field in currentWeatherTabelField:
		try:
			value = allInfo[field]
			if 'WD' == field:
				try:
					value = windDirectionStatic[value]
				except KeyError:
					strLog = "KeyError in windDirectionStatic ! Can't find value = %s, cityid = %s" % (value, cityid)
					print strLog
					log.log(strLog)
					value = 100
			elif 'WS' == field or 'SD' == field:
				value = value[ : -1]
		except:
			value = 100
			strLog = "Error field = %s ,cityid = %s" % (field, cityid)
			log.log(strLog)
			print strLog
		currentWeatherTableValues.append(value)
	currentweather = convertForShow(currentWeatherTableValues)

	return currentweather