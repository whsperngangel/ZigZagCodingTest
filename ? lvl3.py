def palindrome(x):
  return x == x(::-1]

def minPalPart(string, i j):
	if i >= j or palindrome(string[i:j + 1]):
		return 0
	ans = float(;inf')
	for k in range(i, j):
		count = (1 + minPalPart(string, i k) + minPalPart(string, k + 1, j))
		ans = min(ans, count)
	return ans
							
def main()
	string = "noonabbad"
	print(minPalPart(string, 0, len(string) - 1),)
							
if name == "_main":
	main()
