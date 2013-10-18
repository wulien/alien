# -*- coding=cp936 -*-
import xml.dom.minidom

class ReadXml(object):
	def __init__(self, xmlName):
		self.xmlName = xmlName

	def getAllCodes(self):
		dom = xml.dom.minidom.parse(self.xmlName)
		root = dom.documentElement
		nodes = root.getElementsByTagName('code')
		codes = []
		for node in nodes:
			for node in node.childNodes:
				codes.append(node.data)
		return codes

	def getCodeByCityName(self, cityName):
		dom = xml.dom.minidom.parse(self.xmlName)
		root = dom.documentElement
		rows = root.getElementsByTagName('row')
		flag = 0
		for row in rows:
			for node in row.childNodes:
				for one in node.childNodes:
					content = one.data
					if (content == cityName):
						flag = 1
					if 1 == flag:
						code = content
					# content = content.encode('gb2312')
			if 1 == flag:
				break;
		if len(code):
			return code

		return 0

					



if __name__ == '__main__':
	xmlname = 'F:/develop/python/weatherDevelop/cityAndCode.xml'
	codesRead = ReadXml(xmlname)
	cityName = '朝阳'
	cityName = cityName.decode('UTF-8')
	code = codesRead.readCodeByCityName(cityName)
	print code
