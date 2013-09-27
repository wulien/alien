# -*- coding=utf-8 -*-
import MySQLdb
import publicFun


class DBOperation(object):
	def __init__(self, coninfo):
		if (len(coninfo) != 4):
			raise
		self.host = coninfo[0]
		self.user = coninfo[1]
		self.passwd = coninfo[2]
		self.dbName = coninfo[3]
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

	def deleteTable(self):
		with self.con:
			cur = self.con.cursor()
			cur.execute("show tables")
			allTables = cur.fetchall()
			for table in allTables:
				cur.execute("delete from %s" % table)
			print "Delete tables OK!"

	def insertData(self, datas, table):
		with self.con:
			cur = self.con.cursor()
			cur.execute("set names 'gbk'")
			com = "insert into %s values " % table + datas
			strForPrint = unicode(com, 'gbk')
			print "---%s---" % strForPrint
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



if __name__ == '__main__':
	coninfo = ['127.0.0.1', 'root', 'vislecaina', 'weather']
	db = DBOperation(coninfo)
	table = 'basicinfo'
	datas = ('112233445', u'湖北', 'hubei', u'2013年9月27日', u'星期五', 11)
	db.insertData(datas, table)

