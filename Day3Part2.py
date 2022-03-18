with open("Day3input.txt") as rawInput:
    input = rawInput.readlines()
    data = []
    for i in input:
        data.append(i.strip('\n'))

bitlength = len(data[0])

currOxyList = data
currCOList = data
for i in range(bitlength):
    count = 0
    counter = 0
    list1 = []
    list2 = []   
    for n in currOxyList:
        counter += 1
        if (n[i] == '0'):
            list1.append(n)
        else:
            list2.append(n)
            count += 1
    if (count < (counter/2)):
        currOxyList = list1
    else:
        currOxyList = list2
    if len(currOxyList) == 1:
        oxy = currOxyList[0]

for i in range(bitlength):
    count = 0
    counter = 0
    list1 = []
    list2 = []
    for n in currCOList:
        counter += 1
        if (n[i] == '0'):
            list1.append(n)
        else:
            list2.append(n)
            count += 1
    if (count < (counter/2)):
        currCOList = list2
    else:
        currCOList = list1  
    if len(currCOList) == 1:
        co = currCOList[0]
        break 
    print(counter)
    

def binaryToDecimal(binary_num):
    dec_num = 0
    m = 1
    for digit in reversed(binary_num):
        digit = int(digit)
        dec_num += (digit * m)
        m = m * 2
    return dec_num
print(binaryToDecimal(oxy) * binaryToDecimal(co))
