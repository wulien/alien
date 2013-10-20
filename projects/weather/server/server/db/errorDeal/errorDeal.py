import re
def dealError():
    name = 'error.txt'
    fR = open(name, 'r')
    fW = open('result.txt', 'w')
    lines = fR.readlines()
    values = []
    for line in lines:
        nameAndValue = re.split('=', line)
        if len(nameAndValue) == 2:
            value = nameAndValue[1]
            if value not in values:
                fW.write(line)
                values.append(value)
                
    fR.close()
    fW.close()
    
if __name__ == '__main__':
    dealError()
                