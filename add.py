def add(a,b):
	return a + b

x = int(input())
y = int(input())
add(1,2)
f = open("hello.py","a")
for i in range(x,y):
	print("#" + str(add(i,i+1)), file=f)
