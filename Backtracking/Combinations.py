class Solution():
		def combinations(self, S):
				res = []
				def helper(S, start, curr):
						res.append(curr)
						for i in range(start, len(S)):
								helper(S, i + 1, curr + S[i])
				helper(S, 0, '')
				return res

S = '123'
obj = Solution()
print(obj.combinations(S))
