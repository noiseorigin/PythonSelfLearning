## Leetcode Algrithm ZigZag problem
class Solution:
	def convert(self,s,nRows):
		lines = ['']*nRows
		if nRows == 1:
			return s

		period = 2*(nRows - 1)

		for i in range(len(s)):
			index = i % period    ##get the row num
			print(index)
			if index < nRows:
				lines[index] += s[i]
			else:
				lines[period-index] +=s[i] 

		output = ""
		for l in lines:
			output += l
		return output


s = Solution()
print(s.convert("PAYPALISHIRING",3))


## 1   9       17
## 2  810    16
## 3 7 11  15
## 46  1214
## 5   13

# 0   8
# 1  7
# 2 6
# 35 
# 4
