
import MySQLdb
import publicFun
import log

class DBOperation(object):
	def __init__(self, coninfo = ('127.0.0.1', 'root', 'vislecaina', 'weather')):
		self.host = coninfo[0]
		self.user = coninfo[1]
		self.passwd = coninfo[2]
		self.dbName = coninfo[3]
		# else:
		# 	self.host = '127.0.0.1'
		# 	self.user = 'root'
		# 	self.passwd = 'vislecaina'
		# 	self.dbName = 'weather'
		try:
			self.con = MySQLdb.connect(self.host, self.user, self.passwd, self.dbName, charset='gbk')
			print "-----Connect DB OK!-----"
		except MySQLdb.Error:
			print "Connect DB error!"

	def writeDB(self, table, dataForWrite):
		"""dataForWrite is a list contains datas for writing db; The list is a var length"""
		with self.con:
			cur = self.con.cursor()
			cur.execute("DROP TABLE IF EXISTS %s" % table)

	def deleteAllTable(self):
		with self.con:
			cur = self.con.cursor()
			cur.execute("show tables")
			allTables = cur.fetchall()
			for table in allTables:
				cur.execute("delete from %s" % table)
			print "Delete tables OK!"

	def deleteTable(self, table):
		with self.con:
			cur = self.con.cursor()
			cur.execute("delete from %s" % table)
			print "Delete table \'%s\' OK!" % table

	def deleteRowInTable(self, table, cityid):
		with self.con:
			cur = self.con.cursor()
			cur.execute("delete from %s where cityid = \'%s\'" % (table, cityid))
			strLog = "Delete row in table \'%s\' OK, cityid = %s" % (table, cityid)
			log.log(strLog)

	def insertData(self, datas, table):
		with self.con:
			cur = self.con.cursor()
			cur.execute("set names 'gbk'")
			com = "insert into %s values " % table + datas
			# strForPrint = unicode(com, 'gbk')
			# print "---%s---" % strForPrint
			print com
			print type(com)
			cur.execute(com)
			print "-----Insert data OK!-----"

	def readTable(self, table):
		with self.con:
			cur = self.con.cursor()
			cur.execute("select * from %s" % table)
			rows = cur.fetchall()
			for row in rows:
				rowData = publicFun.convertForShow(row)
				print rowData
			print "Read database OK!"
		return rows
		
	def getYesTempByCityId(self, table, cityid):
		with self.con:
			cur = self.con.cursor()
			cur.execute("select temp1Low, temp1High from %s where cityid = \'%s\'" % (table, cityid))
			rows = cur.fetchall()
			if (0 != len(rows)):
				row = rows[0]
				strLog = "Get yesterday temperatur OK, cityid = %s" % cityid
			else:
				strLog = "Get yesterday temperatur failed, cityid = %s" % cityid
				row = (100, 100)
			log.log(strLog)
			print strLog
			# return (yesTempLow, yesTempHigh)
			return row

	def getYesterdayWeather(self, table, cityid):
		with self.con:
			cur = self.con.cursor()
			cur.execute("select yesWeather from %s where cityid = \'%s\'" % (table, cityid))
			rows = cur.fetchall()
			if (0 != len(rows)):
				strLog = "Get yesterday weather OK, cityid = %s" % cityid
				row = rows[0]
			else:
				strLog = "Get yesterday weather failed, cityid  = %s" % cityid
				row = ()
			log.log(strLog)
			print strLog
		return row

	def getYesterdayWind(self, table, cityid):
		with self.con:
			cur = self.con.cursor()
			cur.execute("select yesWind from %s where cityid = \'%s\'" % (table, cityid))
			rows = cur.fetchall()
			if (0 != len(rows)):
				strLog = "Get yesterday wind OK, cityid = %s" % cityid
				row = rows[0]
			else:
				strLog = "Get yesterday wind failed, cityid  = %s" % cityid
				row = ()
			log.log(strLog)
			print strLog
		return row


