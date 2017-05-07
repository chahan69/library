# BIT
# iにxを足すのと0からiまでの合計をlog(n)でできる

n = 10


bit = [0 for i in range(n)]

def sum(i):
	s = 0
	while i > 0:
		s += bit[i]
		i -= i&-i
	return(s)

def add(i, x):
	while i <= n:
		bit[i] += x
		i += i&-i


print(bit)
add(5, 5)
print(bit)
print(sum(8))