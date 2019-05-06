n = int(input())
li = [i for i in range(12,90) if(i%10 > (i//10))]
if n in li and n < 89:
	x = li.index(n)-1
	print(li[x],li[x+2])
else:
	print(li[0],li[-2])
