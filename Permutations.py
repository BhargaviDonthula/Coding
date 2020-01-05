from itertools import permutations
class Permutation():
		def permutate(self, S):
				res = []
				def helper(remaining, curr_str):
						if not remaining:
								res.append(curr_str)
						else:
								for i in range(len(remaining)):
										helper(remaining[ : i] + remaining[i + 1 : ], curr_str + remaining[i])
				helper(S, '')
				return res
S = '123'
print(list(map(''.join, permutations(S))))
obj = Permutation()
print(obj.permutate(S))