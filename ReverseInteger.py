class Solution:

	def reverse(self, x):
		sign = 0;
		if x < 0:
			sign = -1
			x = -1*x
			# print(x)
		elif x > 0:
			sign = 1
		else:
			return 0

		string = str(x)
		# print(string)
		res = string[::-1]
		if(int(res) < pow(2,31)):
			return sign*int(res)
		else:
			return 0


s = Solution()
print(s.reverse(1534236469))