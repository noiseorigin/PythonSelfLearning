##ugly code solving parse phone number question in microsoft code compete

import re
text = ''.join(open('PracticeInput.txt').readlines())

text_file = open("Output.txt", "w")
# text = ''.join(open('test.txt').readlines())
phoneNumbers = re.split(r'\n', text)
with open("Output.txt", "w") as text_file:
	data = ""
	for pn in phoneNumbers:

		elements = re.findall("\d+",pn)
		numLength = 0
		for e in elements:
			numLength = numLength+len(e)

		if pn.startswith('1'):
			chars = list(pn[5:])
			# print(chars)
			newNum =""
			for c in chars:
				if c in ('A','B','C','a','b','c'):
					newNum += '2'
				if c in ('D','E','F','d','e','f'):
					newNum += '3'
				if c in ('G','H','I','g','h','i'):
					newNum += '4'
				if c in ('J','K','L','j','k','l'):
					newNum += '5'	
				if c in ('M','N','O','m','n','o'):
					newNum += '6'
				if c in ('P','Q','R','S','p','q','r','s'):
					newNum += '7'
				if c in ('T','U','V','t','u','v'):
					newNum += '8'
				if c in ('W','X','Y','Z','w','x','y','z'):
					newNum += '9'
				if c in ('1','2','3','4','5','6','7','8','9','0'):
					newNum += c
				else:
					newNum +=""

			# print(newNum)
			# print("+1"+pn[0]+pn[2:5]+newNum)
			if (len(newNum)==7):
				data = "+"+pn[0]+pn[2:5]+newNum
				print(data)
		# print(chars)
		# print(newNum)

		

		# print(numLength)
		elif numLength==11:
			output = "+"
			for e in elements:
				output=output+e
			if(output[1]=='1'):
				data = output
				print(output)
			else:
				data = "Fleshling follow-up needed"
				print("Fleshling follow-up needed")

		elif numLength == 10:
			output = "+1"
			for e in elements:
				output = output + e
			
			data = output
			print(output)

		else:
			data = "Fleshling follow-up needed"
			print("Fleshling follow-up needed")

		text_file.write(data+'\n')
	
text_file.close()

