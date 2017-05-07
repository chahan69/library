class union_find:
	def __init__(self, size):
		# 負の値はルート (集合の代表) で集合の個数
		# 正の値は次の要素を表す
		self.size=size
		self.table = [-(i+1) for i in range(size)]
		self.num=[0 for i in range(size)]

	# 集合の代表を求める O(log(n))
	def find(self, x):
		if self.table[x] < 0:
			self.size+=-1
			return(x)
		else:
			# 経路の圧縮 木の高さ=2
			self.table[x] = self.find(self.table[x])
			return(self.table[x])

	# 併合 O(log(n))
	def unite(self, x, y):
		s1 = self.find(x)
		s2 = self.find(y)
		if s1 != s2:
			if self.table[s1] <= self.table[s2]:
				# 小さいほうが個数が多い
				self.table[s1] += self.table[s2]
				self.table[s2] = s1
			else:
				self.table[s2] += self.table[s1]
				self.table[s1] = s2
			return(True)
		return(False)

	# チェック
	def same(self, x, y):
		if self.find(x)==self.find(y):
			return(True)
		else:
			return(False)

	# 確定 O(nlog(n))
	def definite(self):
		for i in range(self.size):
			self.num[i]=self.find(i)
		return(True)















