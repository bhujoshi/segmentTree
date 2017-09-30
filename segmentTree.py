import math
class SegmentTree	:
	global MAX
	MAX = 10**9
	rangeLength = 0
	def findMiddle(self,s,e):
		return (round((s+e)/2))
		
	def __init__(self,arr):
		self.rangeLength = len(arr)
		power = math.ceil(math.log(self.rangeLength, 2))
		self.r = [None] * (2 ** (power + 1))
		self.constructSegmentTree(arr,0,0,self.rangeLength)
		
	def constructSegmentTree(self,arr,i,s,e):
		if (s == e - 1):
			self.r[i] = arr[s]
		else:
			m = self.findMiddle(s,e)
			self.r[i] = min(self.constructSegmentTree(arr,2*i+1,s,m),self.constructSegmentTree(arr,2*i+2,m,e))
		
		return self.r[i]	
		
	def rangeQueryMain(self,i,s,e,rs,re):
		#print(i,s,e,rs,re)
		if s+1 > re or e < rs:
			return MAX
		if rs <= s+1 and e <= re:
			return self.r[i]
	
		m = self.findMiddle(s,e)
		return  min(self.rangeQueryMain(2*i+1,s,m,rs,re),self.rangeQueryMain(2*i+2,m,e,rs,re))
		
	def rangeQuery(self,queryStart,queryEnd):
		if (queryStart <= 0  or queryStart > queryEnd or queryEnd > self.rangeLength):
			print("Invalid range")
			return 
		return self.rangeQueryMain(0,0,self.rangeLength,queryStart,queryEnd)	
				
		

arr = list(map(int,input().split()))
obj = SegmentTree(arr)
for i in range(int(input())):	
	rs,re = list(map(int,input().split()))
	print(obj.rangeQuery(rs,re))				 