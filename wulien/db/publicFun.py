# -*- coding=utf-8 -*-
def getFieldById(allInfo, tableField):
	tableValues = []
	for field in tableField:
		value = allInfo[field].encode('gbk')
		tableValues.append(value)

	return convertForShow(tableValues)

def convertForShow(tableValues):
	tmp = ''
	i = 0
	while(i < len(tableValues)):
		item = tableValues[i]
		# print type(tableValues[i])
		# print tableValues[i]
		if ('unicode' == type(item)):
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