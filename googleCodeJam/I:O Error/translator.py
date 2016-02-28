def converter(iostring):
	binary = ''
	result = ''
	for bit in iostring:
		if bit == "I":
			binary += "1"
		else:
			binary += "0"

	chars = [binary[x:x+8] for x in range(0,len(binary),8)]

	for c in chars:
		result += chr(int(c,2))

	return result




def main():
	file = open('A-small-practice.in','r')
	testsNum = file.readline()
	count = 0
	for line in file:
		if line[0].isdigit():
			count += 1
		else:
			print("Case #"+ str(count) +" "+ converter(line))





if __name__ == '__main__':
	main()