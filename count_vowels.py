word = raw_input("Enter a word : ")  ##ask for input

count = 0     ## count starts from 0

for w in word:
	if w in ('A','E','I','O','U','a','e','i','o','u'):   ##possible vowels set
		count += 1


result = ' '   ##This is jus for good looking output string
if count == 0:
	result = 'There is no vowel in this word'
elif count == 1:
	retult = 'There is 1 vowel in this word'
else:
	result = 'There are '+ str(count) + 'vowels in this word'
print(result)  ##print the result

