def byteToASCII(bytes):
	byteLength = len(bytes)
	temp = 0
	for i in range(byteLength):
		if(bytes[i] == 'I'):
			temp = temp + pow(2,byteLength-i-1)
		i = i+1
	return chr(temp)

def split_by_size(string, size):
	res = []
	n = len(string)
	for i in range(0,n,size):
		res.append(string[i:i+size])
	return res

text = open('p1_input.txt').read()
lines = text.split('\n')
##print(lines)
caseNum = int(lines[0])
charNums = []
bytes = []
for i in range(len(lines)):
	i = i+1
	if i == 0 or i == len(lines):
		break
	elif i % 2 == 1:
		charNums.append((lines[i]))
	elif i % 2 == 0:
		bytes.append(split_by_size(lines[i],8))

# print(charNums)
# print(bytes)

for b in bytes:
	output = ''
	for bb in b:
		output = output + byteToASCII(bb)
	print(output)





