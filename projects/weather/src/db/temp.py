import re
cityWeather = open("F:/develop/python/weatherDevelop/cityAndWeather.txt", 'r+')
sortedFile = open("sorted.txt", 'w')
content = cityWeather.readlines()
print content
rule = "[\d]{9}"
for name in content:
	citys = re.split(r'[\d]{9}', name)
	codes = re.findall(rule, name)
	# print citys
	# print codes
	codeLen = len(codes)
	print codeLen
	i = 0
	while i < codeLen:
		strings = citys[i] + codes[i]
		sortedFile.write(strings)
		sortedFile.write('\n')
		i += 1

cityWeather.close()
sortedFile.close()
	