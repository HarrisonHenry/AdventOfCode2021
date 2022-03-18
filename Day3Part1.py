with open("Day3input.txt") as rawInput:
    input = rawInput.readlines()
    data = []
    for i in input:
        data.append(i.strip('\n'))

bitlength = len(data[0])
varList = []
for i in range(bitlength):
    varList.append(0)

count = 0
for i in data:
    count += 1
    for n in range(bitlength):
        if(i[n] == '1'):
            varList[n] += 1
gamma = ""
epsilon = ''
for i in varList:
    if (i<(count/2)):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


def binaryToDecimal(binary_num):
    dec_num = 0
    m = 1
    for digit in reversed(binary_num):
        digit = int(digit)
        dec_num += (digit * m)
        m = m * 2
    return dec_num
print(gamma, epsilon)
print(binaryToDecimal(gamma) * binaryToDecimal(epsilon))
