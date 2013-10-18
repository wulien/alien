# -*- coding: utf-8 -*-
import xml.dom.minidom
import codecs
import re

def writeMyXml():
	impl = xml.dom.minidom.getDOMImplementation()
	dom = impl.createDocument(None, 'data', None)
	root = dom.documentElement
	f = open("sorted.txt", 'r')
	content = f.readlines()
	for line in content:
		cityAndCode = re.split(':', line)
		cityname = cityAndCode[0]
		citycode = cityAndCode[1]
		rowNode = dom.createElement('row')
		cityNode = dom.createElement('city')
		codeNode = dom.createElement('code')
		cityName = unicode(cityname, "gbk")

		cityNameNode = dom.createTextNode(cityName)
		codeNameNode = dom.createTextNode(citycode)

		cityNode.appendChild(cityNameNode)
		codeNode.appendChild(codeNameNode)
		
		rowNode.appendChild(cityNode)
		rowNode.appendChild(codeNode)
		root.appendChild(rowNode)
	root.toxml()

	f = open("xmlWrite.xml", 'w')
	writer = codecs.lookup('utf-8')[3](f)
	dom.writexml(writer, encoding = 'utf-8')
	writer.close()

if __name__ == '__main__':
	writeMyXml()