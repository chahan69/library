import bisect,time
# number以上の値が入っているインデクスを返す(bisectより早い)

def binary_search(lis,number):
	start=0
	end=len(lis)-1
	center=int((start+end)/2)
	while end-start>1:
		if lis[center]>=number:
			end=center
			center=int((start+end)/2)
		else:
			start=center
			center=int((start+end)/2)
	return(end)

l=[1,4,5,7,32,342,2455,25462]

t0=time.time()
print(binary_search(l,3))
l.insert(1,3)
print(l)
print(time.time()-t0)